import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(('localhost', 8888))
        print("Successfully connected to the server.")

        while True:
            # Receive message from server (either prompt or response)
            server_message = client_socket.recv(1024).decode().strip()

            # If no message is received, break the loop
            if server_message == "":
                print("No message received from the server.")
                break
            print("\nServer:", server_message)

            # You either guessed correctly, or ran out of tries
            if "Unlucky" in server_message or "Success" in server_message:
                print("Game over. Bye Bye !")
                break # Exit the loop

            # Get input from client
            client_input = input("Enter your guess (or write END to Exit): ").strip()

            if client_input.upper() == "END":
                client_socket.send(client_input.encode())
                print("Client ended the connection.")
                return
            
            # Add placeholder for empty input (So the server can handle it)
            if client_input == "":
                client_input = "EMPTY"

            # Send the input to the server
            client_socket.send(client_input.encode())

    except ConnectionRefusedError:
        print("Couldn't connect to the server.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        client_socket.close()
        print("Client's connection is closed.")

if __name__ == '__main__':
    main()
