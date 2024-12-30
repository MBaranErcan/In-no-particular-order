## CMPE 472_SEC 3 Computer Networks

Name: Mustafa Baran Ercan
No: 2881055520
Date of Submission: 03 /1 1 /202 4


## Table of Contents

- CMPE 472_SEC 3 Computer Networks
   - 1. Introduction
   - 2. Explanation of server.py
      - 2.1. Loading Stock Data and Random Stock Selection
      - 2.2. Validating Guesses and Sending Feedback
   - 3. Explanation of client.py
      - 3.1. Interactions & sending guesses
      - 3.2. Handling Feedback and Terminating Conditions
   - 4. Example Scenarios with Code Snippets
      - 4.1. Scenario 1: Successful Guess
      - 4.2. Scenario 2: Exceeding Guess Limit
      - 4.3. Scenario 3: Wrong Inputs & Ending the Game with Input “END”

---
### 1. Introduction

In this report, the design and implementation of a Python socket programming application for
the "Stock Market Prediction" game is discussed. The program consists of a client that tries to
estimate the stock's price within a tolerance range and a server that picks a stock at random
from an Excel file called "stock.xlsx." The server either ends the connection if requested to or
provides feedback on each guess, allowing up to three attempts per game. Using Python
sockets on a local machine (localhost) on port 8888, this setup demonstrates the basic client-
server communication model.

Example run of the program with correct guess at the end:
![image](https://github.com/user-attachments/assets/7d8012ac-b91b-4c08-93e3-f1a209e26181)

---
### 2. Explanation of server.py

#### 2.1. Loading Stock Data and Random Stock Selection

The server uses the Pandas library for importing stock data from an Excel file (stock.xlsx).
After importing the data, the server chooses a stock at random and delivers it to the client.

![image](https://github.com/user-attachments/assets/ef1cf9c0-7125-4d24-8a74-f034f1f8dc3a)



#### 2.2. Validating Guesses and Sending Feedback

The client is given three chances by the server to guess the stock price with a 5% tolerance.
Depending on whether the guess was accurate, too high, or too low, the server provides
feedback after every guess. The connection ends if the client requests to end the game or runs
out of tries.

![image](https://github.com/user-attachments/assets/f805aa41-a68d-4b78-ac4d-c7e777608aab)


1: Handles user input “END”
2: Handles empty user input (Ps: Client side has empty-input handler for transmission issues)
3: Handles other invalid inputs (negative numbers or strings)
4: Correct guesses
5: Higher price guess than the actual price
6: Lower price guess than the actual price

---
### 3. Explanation of client.py

#### 3.1. Interactions & sending guesses

The client program asks the user to guess the stock price or exit the game by typing "END."
Every guess is transmitted to the server, and the client gets provided with the response.
![image](https://github.com/user-attachments/assets/293226e3-80d3-47e0-adce-f27ad6779be6)


#### 3.2. Handling Feedback and Terminating Conditions

The client decodes server messages for game-ending conditions, hints, or accurate guesses.
Depending on user input or whether the server ends the game, the program ends the
connection.

Server ends the game (Ran out of tries):

![image](https://github.com/user-attachments/assets/93df461b-0389-49a3-adcf-1e80b8dbd738)


User ends the game by writing “END”:

![image](https://github.com/user-attachments/assets/2ad905f0-77fb-48a8-884d-381d92c89d13)


---
### 4. Example Scenarios with Code Snippets

```
(The left side of the images are Client-side, and the right side of the images are Server-side)
```
---
#### 4.1. Scenario 1: Successful Guess

![image](https://github.com/user-attachments/assets/6ebdb850-1845-4d08-910a-b52c147a620a)

---
#### 4.2. Scenario 2: Exceeding Guess Limit

![image](https://github.com/user-attachments/assets/dae7cd05-bb6d-41cc-b5b4-83f3016ed076)

---
#### 4.3. Scenario 3: Wrong Inputs & Ending the Game with Input “END”

![image](https://github.com/user-attachments/assets/ab0bcdf4-cd4b-4593-82ef-fbc207db285c)



