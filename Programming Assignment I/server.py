import socket
import pandas as pd

# Load the stock data from the attached Excel file (stock.xlsx) on the server side
stocks_df = pd.read_excel("stock.xlsx")

def handle_request(client_conn):
    try:
        # Select a random stock
        selected_stock = stocks_df.sample().iloc[0] # sample() returns a random sample
        symbol = selected_stock['Stock Symbol']
        price = selected_stock['Price']  # int

        # Send a message to the client, asking for a price prediction
        tries = 0
        tolerance = 0.05
        message = "Predict the price for {0}\n".format(symbol)
        client_conn.send(message.encode())

        while True:
            try:
                # Get the client's guess
                client_guess = client_conn.recv(1024).decode().strip()  # 1024: buffer size, decode(): bytes to string, strip(): remove whitespaces
                print("Client guessed: {0}".format(client_guess))

                if client_guess.upper() == "END": # Close connection
                    print("Client terminated the connection by sending END.")
                    client_conn.close() # Close the connection
                    print("Client disconnected.\nServer is closing down too...")
                    return # Exit the function

                # Handle empty input
                if client_guess == "EMPTY":
                    print("Client entered empty input.")
                    client_conn.send("Please enter a valid number.\n".encode())
                    continue

                # Validate that the input is a non-negative number
                try:
                    client_guess = float(client_guess)
                    if client_guess < 0:
                        raise ValueError
                except ValueError:
                    client_conn.send("Invalid input. Please enter a non-negative numeric value.\n".encode())
                    continue

                # Check if the guess is within 5% of the actual price
                if abs(client_guess - price) <= price * tolerance: # If is 5%
                    client_conn.send("Success!\n".encode()) # Send a success message
                    print("The client guessed correctly.")
                    break

                elif client_guess < price:  # Higher
                    tries += 1 # Increment the tries
                    if tries >= 3:
                        client_conn.send("Unlucky, the correct price was: {0}\n".format(str(price)).encode())
                        print("The client spent 3 guesses incorrectly.")
                        break
                    else:
                        client_conn.send(("Higher! You have " + str((3-tries)) + " tries left\n").encode())

                else:   # Lower
                    tries += 1 # Increment the tries
                    if tries >= 3:
                        client_conn.send("Unlucky, the correct price was: {0}\n".format(str(price)).encode())
                        print("The client spent 3 guesses incorrectly.")
                        break
                    else:
                        client_conn.send(("Lower! You have " + str((3-tries)) + " tries left\n").encode())

            except ConnectionResetError:
                print("Client disconnected.")
                return



    except Exception as e:
        print("An error occurred: {0}".format(str(e)))
    finally:
        pass # Do nothing and let the client close the connection

def serve_forever():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8888))
    server_socket.listen(5)

    print("Server is running, waiting for connections...")

    while True:
        client_conn, client_addr = server_socket.accept()
        print("Client connected from address {0}".format(str(client_addr)))
        handle_request(client_conn)

if __name__ == '__main__':
    serve_forever()