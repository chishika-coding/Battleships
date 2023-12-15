'''Battleships with Web Interface'''
import json
from flask import Flask, render_template, jsonify, request
from mp_game_engine import (generate_attack, attack, initialise_board,
place_battleships, create_battleships)

player_board = []
computer_board = []
player_ships = {}
computer_ships = {}


app = Flask(__name__)


@app.route('/placement', methods = ['GET', 'POST'])
def placement_interface():
    '''
    [GET] the template for the flask server and allows the use of a graphic interface to
    place ships on a board. Saves this placement.
    [POST] Opens the saved placements to start creating the player and computers boards
    and ships.
    '''
    global player_board, player_ships, computer_board, computer_ships
    player_ships = create_battleships()
    board_size = 10

    if request.method == 'GET':
        print('\nGET Request to placement.html \n')
        return render_template("placement.html", ships = player_ships, board_size = board_size)

    if request.method == 'POST':
        placement = request.get_json()
        print('\nOpening json and saving data from POST at placement.html \n')
        with open('web_placement.json', 'w', encoding="utf-8") as file:
            json.dump(placement, file, indent=4)
        print('Finished with json')
        player_board = initialise_board(board_size)
        place_battleships(player_board, player_ships, 'custom', 'web_placement.json')
        print('\nInitialised player_board and player_ships for player \n')
        #display_board(player_board)

        #with open('player_board.json', 'w') as file:
            #json.dump(player_board, file, indent=1)

        computer_board = initialise_board(board_size)
        computer_ships = create_battleships()
        place_battleships(computer_board, computer_ships, 'random')
        print('\nInitialised player_board and player_ships for computer \n')

        return jsonify({"message": "Success"})

    return None

@app.route('/attack', methods = ['GET'])
def process_attack():
    '''
    Processes the users attack from the grid and then processes the AIs attack, and
    returns a message updating the player and the boards with the attack. Also mentions 
    if game has been won or lost when finished.
    '''
    if request.args:
        x = request.args.get('x')
        y = request.args.get('y')
        coordinates = (x,y)
        print('\nPlayer selected', coordinates)
        hit = attack(coordinates, computer_board, computer_ships)

        aicoordinates = generate_attack()
        print('\nComputer selected', aicoordinates)
        attack(aicoordinates, player_board, player_ships)


        if computer_ships == {}:
            print('\nPlayer won')
            return jsonify ({"hit": hit, "AI_Turn": (aicoordinates), "finished": "VICTORY"})
        if player_ships == {}:
            print('\nComputer won')
            return jsonify ({"hit": hit, "AI_Turn": (aicoordinates), "finished": "DEFEAT"})

        return jsonify ({"hit": hit, "AI_Turn": (aicoordinates)})

    return None

@app.route('/', methods = ['GET'])
def root():
    '''
    Renders the main page of the program with the grids for the player to interact with.
    '''


    return render_template("main.html", player_board = player_board)




if __name__ == '__main__':
    app.template_folder = 'templates'
    app.run()
