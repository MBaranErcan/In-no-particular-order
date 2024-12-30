import sys

class Servermy:
    # define variables
    def __init__(self) -> None:
        self.domain = 4
        self.type = 1
        self.protocol = 1
        

    def socketcreator(self, client): # Needs to take the client object for comparison
        if client.domain != self.domain: # If domain is not 4
            errorType = "domain"
        elif client.type != self.type: # If type is not 1
            errorType = "type"
        elif client.protocol != self.protocol: # If protocol is not 1
            errorType = "protocol"
        else:
            print("server is created") # If all of the above is true
            print("Server: Server is Listening")
            return 1
        print(f"{errorType} number is not true") # If any of the above is not true
        return 0
        

    def serveraccept(self, client): # client is the client object
        if client.port == 9000 and client.address == "9000-9000": # If the port number is 9000 and address is 9000-9000 (by default it is)
            print("Server: Connected to the server")
        else:
            print("Server: Connection denied") 
            sys.exit()


    def serverreader(self, message):
        # take the client message and decide the action
        print("Server: Client Address= 9000-9000 , 9000")
        if message == "end":
            print("Server: Server closed")
            sys.exit()
        elif message == "Access9000":
            print("Server: Message is Access9000 access permitted")
        else:
            print("Server: Access denied")


class Clientmy:

    def __init__(self): # define variables
        self.domain = None
        self.type = None
        self.protocol = None
        self.address = "9000-9000" # default address
        self.port = None
    

    def clientcreator(self):
        print("client is created")  # If all of the above is true
        print("Client: Client is ready to connection")
        return self
    
    
    def connect(self): 
        # while the input is not a number, ask again for a number
        print("Client: Send connection demand to the server")
        while True:
            try:
                self.port = int(input("Client: Enter the port number: "))   # Take the port number
                break
            except ValueError:
                print("Please enter a number") # If the input is not a number ask again

        return self # Return the client object, not only port number
    

    def clientwriter(self):
        # take the message and send it to the serverreader
        message = input("Client: Enter the message: ")
        return message



if __name__ == "__main__":
    server = Servermy()
    client = Clientmy()

    # I decided to set the server numbers are fixed and client numbers are obtained from the user
    client.domain = int(input("Enter domain number: "))
    client.type = int(input("Enter type number: "))
    client.protocol = int(input("Enter protocol number: "))

    if server.socketcreator(client) and client.clientcreator():
        server.serveraccept(client.connect())
        while True:
            message = client.clientwriter()
            server.serverreader(message)
