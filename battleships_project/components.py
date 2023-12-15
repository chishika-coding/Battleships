'''Core components the rest of the modules will import from.'''
import random
import json
Boardtype = list[list[str | None]]
def display_board(board: Boardtype, size: int = 10) -> None:
    ''' 
    Function used to check the board state in a visual manner using printlines.

    :param board: a list of lists used to simulate a grid
    :param size: a integer to define size of the grid, defaults to 10
    '''
    for row in board:
        print(' | '.join([' ' if cell is None else str(cell) for cell in row]))
        print('-' * (size * 4 - 1))

def initialise_board(size: int = 10) -> Boardtype:
    ''' 
    Function used to initial a board based on the size chosen. It creates a list of lists.
    
    :param size: an integer to define size of the grid, defaults to 10
    '''
    board = [[None] * size for x in range(size)]

    return board

def create_battleships(filename: str = "battleships.txt") -> dict[str, int]:
    '''
    Function used to create battleships based on the battleships.txt file and
    saves it as a dictionary.

    :param filename: Name of the text file, defaults to "battleships.txt"
    '''
    ships = {}
    with open(filename, "r", encoding='utf-8') as shipfile:
        for line in shipfile:
            shipname, shiplength = line.split(':')
            ships= {**ships, shipname: int(shiplength)}
    return ships


def place_battleships(board: Boardtype, ships: dict[str, int],
                      style: str = 'simple', algorithm: str = "Easy",
                      battleshipjson: str = 'placement.json') -> Boardtype:
    '''
    Used to choose the right placement function to call

    :param board: a list of lists used to simulate a grid
    :param ships: a dictionary to hold the battleships and their lengths
    :param style: a string to define what placement function is to be called,
        defaults to 'simple'
    :param algorithm: a string to determine the difficulty of the random placement,
        defaults to 'Easy'
    :param battleshipjson: a string to point towards the correct json file to use
        for custom placements, defaults to 'placement.json'
    '''

    if style == 'simple':
        place_battleships_simple(board, ships)
    elif style =='random':
        place_battleships_random(board, ships, algorithm)
    else:
        place_battleships_custom(board, ships, battleshipjson)

    return board

def place_battleships_simple(board: Boardtype, ships: dict[str, int]) -> None:
    '''
    Places the battleships in a simple formation starting in the top left corner

    :param board: a list of lists used to simulate a grid
    :param ships: a dictionary to hold the battleships and their lengths
    '''

    y = 0
    for current in ships:
        for x in range(ships.get(current)):
            board[y][x] = current
        y +=1

def place_battleships_random(board: Boardtype, ships: dict[str, int],
                            algorithm: str) -> None:
    '''
    Places the battleships in a random pattern inside the board. This has different
    difficulty levels chosen by the algorithm that makes the placements more strategic.

    :param board: a list of lists used to simulate a grid
    :param ships: a dictionary to hold the battleships and their lengths
    :param algorithm: a string to determine whether to place ships more strategically
        or not
    '''
    size = len(board) - 1

    for current in ships:
        validplacement = False
        while not validplacement:
            validplacement = True
            #Valid Placement here ensures if the random coordinates end up causing an overlap with
            #any part of the battleships it won't move on to the next ship and stay here. Another
            #case they flag up is when the longer battleships are placed in the centre.
            rotation = random.choice(["h", "v"])

            if rotation == 'h':
                if algorithm == "Hard":
                    if ships.get(current) > 3:
                        #The purpose of the ship length checks is to increase difficulty, by placing
                        #shorter battleships near the centre area to be hidden, and the longer ones
                        #near the outskirts.

                        x = random.randint(0, (size-ships.get(current)))
                        y =random.randint(0,size)
                        if ((round(size/3)) <= y <=
                            (size - round(size/3))):
                            validplacement = False

                    elif ships.get(current) < 4:
                        x = random.randint(0, (size-ships.get(current)))
                        y =random.randint((round(size/4)),
                                          (size - round(size/4)))
                else:
                    x =random.randint(0,(size-ships.get(current)))
                    y =random.randint(0,size)

            elif rotation == 'v':
                if algorithm == "Hard":
                    if ships.get(current) > 3:
                        y = random.randint(0, (size-ships.get(current)))
                        x =random.randint(0,size)
                        if ((round(size/3)) <= x <=
                            (size - round(size/3))):
                            validplacement = False

                    elif ships.get(current) < 4:
                        y = random.randint(0, (size-ships.get(current)))
                        x =random.randint((round(size/4)),
                                          (size - round(size/4)))
                else:
                    y =random.randint(0,(size-ships.get(current)))
                    x =random.randint(0,size)


            validx, validy = x, y
            #This section checks if each segment is in a empty tile, and uses rotation to know where
            #the next segments should be and check their validity. Validx and y are used so that
            # the real x and y coordinates are unaffected to avoid a list index error.

            #print(current,x,y,rotation)
            for _ in range(ships.get(current)):
                if board[validy][validx] is not None:
                    #print("Invalid\n\n")
                    validplacement = False
                elif rotation == 'h':
                    validx += 1
                elif rotation == 'v':
                    validy += 1

            if validplacement is True:
                for _ in range(ships.get(current)):
                    board[y][x] = current
                    if rotation == 'h':
                        x += 1
                    if rotation == 'v':
                        y += 1

def place_battleships_custom(board: Boardtype, ships: dict[str, int],
                             battleshipjson: str) -> None:
    '''
    Opens the json file specified by its parameters it to decide where 
    to place the battleships.

    :param board: a list of lists used to simulate a grid
    :param ships: a dictionary to hold the battleships and their lengths
    :param battleshipjson: a string to point towards the correct json file to use
        for custom placements, defaults to 'placement.json'
    '''

    with open(battleshipjson) as shipjson:
        shipfile = json.load(shipjson)

    for shipname, shipdata in shipfile.items():
        validplacement = False
        while not validplacement:
            validplacement = True
            #print(shipname, shipdata[0], shipdata[1], shipdata[2])
            x, y, rotation = int(shipdata[0]), int(shipdata[1]), shipdata[2]
            validx, validy = x, y
            for _ in range(ships.get(shipname)):
                if board[validy][validx] is not None:
                    #print("Invalid\n\n")
                    validplacement = False
                elif rotation == 'h':
                    validx += 1
                elif rotation == 'v':
                    validy += 1

        if validplacement is True:
            for _ in range(ships.get(shipname)):
                board[y][x] = shipname
                if rotation == 'h':
                    x += 1
                if rotation == 'v':
                    y += 1


if __name__ == '__main__':
    userboard = initialise_board()
    userships = create_battleships()
    place_battleships(userboard, userships, "custom", 'Hard')
    display_board(userboard)
