#__________________________________________________________________________________________
# Name:             Kristina Montanez
# Date:             1/23/2022
# Class:            CS 372
# Project:          1 - Sockets and HTTP
# File:             http_client_1.py
# Description:      Three python socket programs: (1) simple python program that uses a socket
#                   to interact with a server, using PYTHON SOCKET API; (2) socket program to
#                   receive arbitrarily large files; and (3) listening socket bound to
#                   ‘127.0.0.1’ or ‘localhost’, and a random port number.
#__________________________________________________________________________________________
#
#   TABLE OF CONTENTS:
#
#   1)  SOURCES CITED
#   2)  MODULE IMPORTS
#   3)  PROJECT CODE
#__________________________________________________________________________________________

#   1)          SOURCES CITED
#___________________________________

#   (1)         Code Sample "TCPClient.py"
#   Source:     Kurose, James; Keith W. Ross, "Computer Networking-A Top-Down Approach".
#               Chapter 2, Section 7,
#   Date used:  1/23/2022
#   Note:       Base code that the vast majority of this program uses-slightly
#               modified to fit the assignment

#   (2)         Why only port 80 for web services?
#   Source:     https://networkengineering.stackexchange.com/questions/1976/why-only-port-80-for-web-services
#   Date used:  1/23/2022
#   Note:       Just background for why we need to use Port 80.

#   (3)         Ed Discussion
#   Source:     https://edstem.org/us/courses/16852/discussion/1006512
#   Date used:  1/23/2022
#   Note:       iterate through length of modifiedSentence for length of server response.


#   2)  MODULE IMPORTS
#___________________________________
from socket import *


#   3)  PROJECT CODE
#___________________________________

# Just as in the textbook sample code, set up the
# server's name and set the port to 80, as Source (2)
# explains for default ports for HTTP.
serverName = "gaia.cs.umass.edu"
serverPort = 80

# Now we create the client socket. The AF_INET lets us
# know that we are using "IPv4".
clientSocket = socket(AF_INET, SOCK_STREAM)

# Now we connect to the sever!
clientSocket.connect((serverName, serverPort))

# Here, instead of using "raw_input" (like in the textbook-
# example code), we will ask for the wireshark file1.
sentence = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

# print to the console that we requested the file,
# as required in the assignment screenshot.
print("Request:", sentence)

# We now send our sentence (GET request) through the client's
# socket, into the TCP connection.
clientSocket.send(sentence.encode())

# Now, we take what the server hands back to us and
# place them in a new string.
modifiedSentence = clientSocket.recv(1024)

# Per assignment and Ed Discussion (Source (3)), we need to print out the
# number of bytes/length for the response.
print("[RECV] - length:", len(modifiedSentence))

# print the response out to the console.
print(modifiedSentence.decode())


# We now close the socket connection.
clientSocket.close()



