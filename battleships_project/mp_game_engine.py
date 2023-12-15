'''2 Player Battleships against the computer'''
import random
from game_engine import (cli_coordinates_input, attack,
display_board, initialise_board, create_battleships, place_battleships)
playerboard = []
playerships = {}
computerboard = []
computerships = {}
guesses = []

players = {'Player 1': [playerboard, playerships], 'Computer': [computerboard, computerships]}

def generate_attack(algorithm: str = "Easy", size: int = 10) -> tuple[int, int]:
    '''
    Generates x and y int values for computers turn and returns them as a tuple.

    :param algorithm: a string to determine the difficulty of the random placement,
        defaults to 'Easy'
    :param size: a integer to define size of the grid, defaults to 10
    '''
    global guesses
    validxy = False
    while not validxy:
        validxy = True
        x = random.randint(0,(size-1))
        y = random.randint(0,(size-1))

        if algorithm != 'Easy':
            if [x,y] in guesses:
                validxy = False
            else:
                guesses.append([x,y])

        #This guesses array is to keep track of the moves made by generate_attack
        #and ensure that it does not repeat moves. This puts the user on a timer
        #as the guesses will close in slowly.

    return ( int(x), int(y))

def ai_opponent_game_loop() -> None:
    '''
    Uses the functions to create and run the Battleship program against the computer.
    '''
    global playerboard, computerboard, playerships, computerships
    print("""
    BBBB   AAAAA TTTTTTT  TTTTTTT  L       EEEEE   SSSSS  H   H  IIIII  PPPPP    SSSSS
    B   B  A   A    T        T     L       E      S       H   H    I    P    P  S
    BBBB   AAAAA    T        T     L       EEEE    SSS    HHHHH    I    PPPPP    SSSS
    B   B  A   A    T        T     L       E          SS  H   H    I    P            SS
    BBBB   A   A    T        T     LLLLLL  EEEEE  SSSSS   H   H  IIIII  P        SSSSS    Multiplayer Edition


    Welcome to Battleships

    [Using placements from placement.json file]
    [Ensure you change this until satisfied]

    """)

    algorithm = None
    while algorithm not in ('Easy', 'Medium', 'Hard'):
        if algorithm is not None:
            print('\nEnter a listed difficulty')
        algorithm = input('\n\nSelect your difficulty: \n-Easy \n-Medium \n-Hard \n\n')

    playerboard = initialise_board()
    playerships = create_battleships()
    place_battleships(playerboard, playerships, 'custom')

    computerboard = initialise_board()
    computerships = create_battleships()
    place_battleships(computerboard, computerships, 'random', algorithm)

    sunk = False
    while not sunk:
        print('\n\nTurn:', list(players.keys())[0],' \n\n')
        coordinates = cli_coordinates_input()
        attack(coordinates, computerboard,computerships)


        if computerships == {}:
            print("""
            V     V  IIIII   CCCCC  TTTTTTT   OOOOO   RRRRR   Y     Y
            V     V    I    C          T     O     O  R    R   Y   Y 
             V   V     I    C          T     O     O  RRRR       Y  
              V V      I    C          T     O     O  R   R      Y  
               V     IIIII   CCCCC     T      OOOOO   R    RR    Y  
            """)
            sunk = True

        else:
            print('\n\nTurn:', list(players.keys())[1],' \n\n')
            aicoordinates = generate_attack()
            attack(aicoordinates, playerboard,playerships)
            print("\n\nPlayer's Board\n")
            display_board(playerboard)

            if playerships == {}:
                print('\n\n          Game Over\n\n')
                sunk = True

if __name__ == '__main__':
    ai_opponent_game_loop()
