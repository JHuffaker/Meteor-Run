# Overview

This program is a game created with Python Arcade that utilizes networking to allow two players to play a multiplayer game together as long as they are on the same network. Prior to this program, I had no experience with networking, and so I took this project on to dip my toes in it.

The program has a server file that opens a connection for the client to connect to. It only allows to clients to connect. The client file renders the game for the user and sends the player's coordinates through the network file to the server, and receives the coordinates of the other play as well so that the game can render the correct coordinates of that opposite player.

To run the server, the user will only need to run server.py. To run the client, the user will only need to run client.py, but will also need to have network.py and the images in the same folder.

[Game Demo](https://youtu.be/p3PlJz2Zy8g)

# Network Communication

The program uses a client/server architecture. It uses TCP to transport data. Its port number is 5555. The messages sent between client through the server are tuples sent as strings.

# Development Environment

To develop this software, I used Visual Studio Code, and wrote it in Python 3.9. I used the Python Arcade library, and used sockets and threading for the server.

# Useful Websites

* [Python Arcade](https://arcade.academy)
* [Python 3.9 Documentation](https://docs.python.org/3/)
* [Multiplayer Game Development Tutorial](https://www.youtube.com/watch?v=McoDjOCb2Zo&t=1015s)

# Future Work

* Include meteors that the players have to dodge.
* Include winner/loser screen.
* Have players wait for each other before starting the game.
