'''Battleships with Web Interface'''
import json
from flask import Flask, render_template, jsonify, request
from mp_game_engine import (generate_attack, attack, initialise_board,
place_battleships, create_battleships)

board = []
board2 = []
ships = {}
ships2 = {}


app = Flask(__name__)


@app.route('/placement', methods = ['GET', 'POST'])
def placement_interface():
    '''
    The following # lines are all an alternative answer that requires a board.json file to
    write to and read from later, but the global method seemed cleaner hence I used that 
    instead.
    '''
    global board, ships, board2, ships2
    ships = create_battleships()
    board_size = 10

    if request.method == 'GET':
        print('\nGET Request to placement.html \n')
        return render_template("placement.html", ships = ships, board_size = board_size)

    if request.method == 'POST':
        placement = request.get_json()
        print('\nOpening json and saving data from POST at placement.html \n')
        with open('web_placement.json', 'w', encoding="utf-8") as file:
            json.dump(placement, file, indent=4)
        print('Finished with json')
        board = initialise_board(board_size)
        place_battleships(board, ships, 'custom', 'web_placement.json')
        print('\nInitialised board and ships for player \n')
        #display_board(board)

        #with open('board.json', 'w') as file:
            #json.dump(board, file, indent=1)

        board2 = initialise_board(board_size)
        ships2 = create_battleships()
        place_battleships(board2, ships2, 'random')
        print('\nInitialised board and ships for computer \n')

        return jsonify({"message": "Success"})

    return None

@app.route('/attack', methods = ['GET'])
def process_attack():
    '''
    Hello
    '''
    print("hello")
    if request.args:
        x = request.args.get('x')
        y = request.args.get('y')
        coordinates = (x,y)
        print('\nPlayer selected', coordinates)
        hit = attack(coordinates, board2, ships2)
        
        aicoordinates = generate_attack()
        print('\nComputer selected', aicoordinates)
        attack(aicoordinates, board, ships)
        

        if ships2 == {}:
            print('\nPlayer won')
            return jsonify ({"hit": hit, "AI_Turn": (aicoordinates), "finished": "VICTORY"})
        if ships == {}:
            print('\nComputer won')
            return jsonify ({"hit": hit, "AI_Turn": (aicoordinates), "finished": "DEFEAT"})

        return jsonify ({"hit": hit, "AI_Turn": (aicoordinates)})

    return None

@app.route('/', methods = ['GET'])
def root():
    '''
    hello
    '''

    #with open('board.json', 'r') as file:
                #board = json.load(file)


    return render_template("main.html", player_board = board)




if __name__ == '__main__':
    app.template_folder = 'templates'
    app.run()
