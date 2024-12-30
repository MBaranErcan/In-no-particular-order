

# CMPE 472 Computer Networks

Name: Mustafa Baran Ercan  
Date of Submission: 26/11/2024

Table of Contents

[CMPE 472_SEC 3 Computer Networks 1](#_Toc183553085)

[1\. Introduction 3](#_Toc183553086)

[2\. Explanation of algorithm 3](#_Toc183553087)

[2.1. _Servermy_ _Class_ 3](#_Toc183553088)

[2.2. _Clientmy_ _Class_ 4](#_Toc183553089)

[3\. Conclusion 4](#_Toc183553090)

## Introduction

This work simulates how a client-server system works using Python for UDP socket programming. The server and client classes are designed to handle connection validation, error handling, and message exchange. 


## Explanation of algorithm

### _Servermy_ _Class_

The _Servermy_ class is the class that is responsible for confirming the connection information and processing client messages. Its methods include:

- **\__init_\_:**  
    Initializes the server with default attributes: domain = 4, type = 1, and protocol = 1.  

- **socketcreator(self, client):**  
    Compares the server’s default domain, type, and protocol values against the client’s.
  - If any value does not match, the server prints an error message specifying the invalid attribute and terminates the connection.
  - If everything is correct, the server continues to the reading message state.  

- **serveraccept(self, client):**  
    Validates the client's address (default 9000-9000) and port (9000).
  - If valid, the server acknowledges the connection.
  - Otherwise, the program exits with a rejection message.  

- **serverreader(self, message):**  
    Handles client messages:
  - If the message is "Access9000", access granted.
  - If the message is "end", server shuts down.
  - For other messages, server denies the access.

### _Clientmy_ _Class_

The Clientmy class is responsible for providing connection details and sending messages to the server. Its key methods are:

- **\__init_\_:**  
    Initializes default attributes: domain, type, and protocol and fixed address 9000-9000. These attributes except address, which is fixed, are obtained from the user to be compared with the server’s.  

- **clientcreator(self):**  
    Specifies successful creation of the client and readiness to connect.  

- **connect(self):**  
    Prompts the user to input a port number, validates it, and returns the client object for further use.  

- **clientwriter(self):**  
    Accepts a message from the user and sends it to the server for processing.
