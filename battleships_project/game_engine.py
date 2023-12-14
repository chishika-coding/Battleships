'''
Game Engine used to create a draft of 1-player battleship with no opponent. 
Functions from here are used in later modules
'''
from components import initialise_board, create_battleships, place_battleships, display_board
Boardtype = list[list[str | None]]
def attack(coordinates: tuple[int, int], board: Boardtype, battleships: dict[str, int])-> bool:
    '''
    Checks if the board supplied to it has a battleship at tile where the coordinates
    point and if so removes 1 from the dictionary that contains the current ships.
    If it decreases to 0 removes the key value pair entirely from the given
    dictionary.
    '''
    x, y = int(coordinates[0]), int(coordinates[1])
    if board[y][x] is not None:
        print('\nHit!\n')

        battleships.update({board[y][x]: (battleships.get(board[y][x])-1)})
        if battleships.get(board[y][x]) == 0:
            print('\nBattleship Sunk!\n')
            battleships.pop(board[y][x])
        board[y][x] = None
        return True

    print('\nMiss')
    return False

def cli_coordinates_input(size: int = 10) -> tuple[int, int]:
    '''
    Asks user to input coordinates for the location to attack. Checks if the
    supplied coordinates are valid and looping until they are before
    returning them as a tuple.
    '''
    valid = False
    while not valid:
        x = input(f'\n\n\nEnter X coordinate between 1 - {size}: ')
        y = input(f'\nEnter Y coordinate between 1 - {size}: ')
        try:
            x = int(x)-1
            y = int(y)-1
            if  0 <= x <= (size-1) and 0 <= y <= (size-1):
                valid = True
            else:
                print('\nA supplied integer is not in range \n')

        except ValueError:
            print('\nSupplied an incorrect data type - Must be integer \n')
    return (int(x), int(y))


def simple_game_loop() -> None:
    '''
    Used for intermediate manual testing in the interface. Allows for a single player
    testing of the functions produced so far in a draft version.
    '''
    print("""
    BBBB    AAAA  TTTTTTT  TTTTTTT  L       EEEEE   SSSSS  H   H  IIIII  PPPPP    SSSSS
    B   B  A    A    T        T     L       E      S       H   H    I    P    P  S
    BBBB   AAAAAA    T        T     L       EEEE    SSS    HHHHH    I    PPPPP    SSSS
    B   B  A    A    T        T     L       E          SS  H   H    I    P            SS
    BBBB   A    A    T        T     LLLLLL  EEEEE  SSSSS   H   H  IIIII  P        SSSSS
    """)
    print('\n      Welcome to Battleships \n\n')


    originalboardstate = initialise_board()
    board = initialise_board()
    ships = create_battleships()
    for currentboard in (originalboardstate, board):
        place_battleships(currentboard, ships, style = "simple")
    #display_board(board)
    sunk = False
    while not sunk:
        coordinates = cli_coordinates_input()

        attack(coordinates, board,ships)

        if ships == {}:
            print('\n\n          Game Over\nActual Board\n')
            display_board(originalboardstate)
            sunk = True

        #else:
         #   display_board(board)
          #  print(ships)

if __name__ == '__main__':
    simple_game_loop()
