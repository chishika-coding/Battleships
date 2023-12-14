# README

# Battleships Program

This project is a python implementation of the game Battleships. Battleships is game involving 2 parties where each player places 5 ships of varying sizes and ranks onto a 10x10 grid. These grids are not shown to the opposing party and then the players take turns launching attacks at coorinates on the 10x10 grid where they believe the opposition has placed their battleships. If the location contains a ship segment, a Hit is announced, otherwise a Miss. When a battleship is sunk it is announced and the first to sink all of the opposition's battleships is determined as the winner.

Stretch Goals Achieved
- Improving the AI opponent.
The AI opponent can be customised to be at different levels of difficulty, ranging from Easy, Medium and Hard. Easy is the default used for the web interface, which can be modified by altering the related functions manually in the code. Medium will prevent the AI opponent from making repeat moves by tracking it the generate_attack function. Hard will change the random placements of ships in place_battleships to be more strategic, larger battleships on the outskirts and smaller ones near the centre.

# Prerequisites
Ensure you have the following prerequisites installed:
-Python version for development: Python 3.11 (64-bit)

Dependencies are in the requirements.txt file.


# Installation and Running

To install the dependencies in VSCode, open the terminal and execute
`python3.11 -m pip install -r requirements.txt`

# Getting Started Tutorial

The program can be played VSCode terminal, or alternatively on a local server with a web interface with grids to visualise board states. To begin, open battleships_project folder using VSCode or similar software. 
From here, to play against an AI opponent, run the mp_game_engine.py. 
To access the version with web interface, run main.py and find the URl to the local server the terminal outputs. This should look like http://127.0.0.1:5000. Add /placement to this URl you are given (e.g. http://127.0.0.1:5000/placement) and open in an incognito tab. 
To change difficulty algorithms for the web interface version, in main.py alter the function generate_attack and place_battleships by adding 'Medium' or 'Hard' to the list of arguments.

# Testing
- In VSCode open the battleships_project folder. 
- Select Testing from the menu on the left, select Configure Python Tests 
- Select pytest framework and select the tests directory. 

The tests should now show up on the Testing section and can be run all at once or individually.


# Developer Deconstruction


# Details
This project was the coursework task for ECM1400 Comp Sci BSC University of Exeter. [GitHub Repository](https://github.com/bakapaka/Battleships)


