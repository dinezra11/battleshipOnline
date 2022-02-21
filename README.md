# battleshipOnline
This is the classic Battleship board game, implemented in python using the PyGame library.
For those who aren't familiar with this game, it is a competitive game for 2 players, fighting themselves
At the beginning of the game, each player place his/her battleships inside a 10x10 board. The goal is to guess the other player's battleships placement.
The player who kills all of the enemy's battleships, is the winner of the match.

This repository will include both of the server code and client code. (And of course, the whole game's logic)
I'm kipping both of the server and client code to communicate in the local machine (localhost), so anyone who wants to clone this project and run it will be able
to do so without the limitation of a specific real server.

# Server deployment:
The server is planned to be deployed to my virtual machine instance in Oracle's Cloud.
The database I'm using for this project is SQLite, which also will be held in the cloud with the server code.

# Last Notes:
This project was programmed by me (Din Ezra) for educational purposes only. My goal here is to practice implementing client-server development using TCP sockets, and
developing a multi-threaded application in python.
