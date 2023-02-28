#__________________________________________________________________________________________
# Name:             Kristina Montanez
# Date:             1/23/2022
# Class:            CS 372
# Project:          1 - Sockets and HTTP
# File:             http_server.py
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

#   (1)         Code Sample "TCPServer.py"
#   Source:     Kurose, James; Keith W. Ross, "Computer Networking-A Top-Down Approach".
#               Chapter 2, Section 7,
#   Date used:  1/23/2022
#   Note:       Base code that the vast majority of this program uses-slightly
#               modified to fit the assignment

#   (2)         Python socket programming Tutorial – How to Code Client and Server
#   Source:     https://www.binarytides.com/python-socket-programming-tutorial/
#   Date used:  1/23/2022
#   Note:       A good example used for this program's error handling.

#   (3)         Python – Binding and Listening with Sockets
#   Source:     https://www.geeksforgeeks.org/python-binding-and-listening-with-sockets/
#   Date used:  1/23/2022
#   Note:       An example of setting up a socket, with possible error handling.

#   (4)         "Socket Programming HOWTO"
#   Source:     Python Software Foundation. https://docs.python.org/3/howto/sockets.html
#   Date used:  1/23/2022
#   Note:       A "how to" example of setting up a socket.


#   2)  MODULE IMPORTS
#___________________________________
from socket import *


#   3)  PROJECT CODE
#___________________________________

# Connect to host with designated HTTP port.
serverPort = 1133

# Required data to send off, per assignment details.
data =  "HTTP/1.1 200 OK\r\n"\
        "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
        "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"


# From the materials in the textbook, create the TCP socket and associate
# the server port number. Then, after creating the "welcoming door" as the
# textbook calls it, listen for a client.
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


while True:
    # From the textbook, we will first accept for client server socket.
    connectionSocket, addr = serverSocket.accept()
    serverReceive = connectionSocket.recv(1024).decode()

    try:
        # Attempt to send off the data, if it sends correctly,
        # the console will print out our host and port number,
        # and the GET we received.
        connectionSocket.send(data.encode())
        print('Connected by', connectionSocket.getsockname())
        print('\r\nReceived:', serverReceive)

        # as shown in the example, print out the data to the console
        # with dividers, showing the html sent.
        print("Sending>>>>>>>>")
        print(data)
        print("<<<<<<<<")
        break

    # In the need to deal with errors, Source (2) helped to figure
    # out the exception handling below:
    except socket.error as msg:
        print('Failed to create socket. Error code: ' + str(msg[0]))
        print('\r\nError message : ' + msg[1])
        break

    # as shown in the textbook, close the connection once done with
    # sending the data (or error handling).
    connectionSocket.close()