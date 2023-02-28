#__________________________________________________________________________________________
# Name:             Kristina Montanez
# Date:             1/23/2022
# Class:            CS 372
# Project:          1 - Sockets and HTTP
# File:             http_client_2.py
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
#               modified to fit the assignment. I also indirectly looked at the server example
#               for how to detect when recv or read return <= 0 bytes in a loop.

#   (2)         Why only port 80 for web services?
#   Source:     https://networkengineering.stackexchange.com/questions/1976/why-only-port-80-for-web-services
#   Date used:  1/23/2022
#   Note:       Just background for why we need to use Port 80. Figured this out during
#               writing program for http_client_1.py.

#   (3)         Ed Discussion
#   Source:     https://edstem.org/us/courses/16852/discussion/1006512
#   Date used:  1/23/2022
#   Note:       iterate through length of modifiedSentence for length of server response.
#               also used for http_client_1.py.


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
# example code), we will ask for the longer file; wireshark file3.
sentence = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

# print to the console that we requested the file,
# as required in the assignment screenshot.
print("Request:", sentence)

# We now send our sentence (GET request) through the client's
# socket, into the TCP connection.
clientSocket.send(sentence.encode())

# Now, we take what the server hands back to us and
# place them in a new string.
modifiedSentence = clientSocket.recv(1024)

# create a string that we can place the decoded data.
stringHolder = modifiedSentence.decode()

# now, as the assignment explains, we detect when recv or
# read return <= 0 bytes in a loop.
while len(modifiedSentence) > 0:
    # First, put the info in modifiedSentence so that we can
    # add it to our placeholder, and count the bytes/length at the
    # end of the response.
    modifiedSentence = clientSocket.recv(1024)
    # put the data into our placeholder.
    stringHolder = stringHolder + modifiedSentence.decode()

# Per assignment and Ed Discussion (Source (3)), we need to print out the
# number of bytes/length for the response.
print("[RECV] - length:", len(stringHolder))

# print the response out to the console.
print(stringHolder)

# We now close the socket connection.
clientSocket.close()
