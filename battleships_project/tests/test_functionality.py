import pytest
import random
from components import place_battleships_random
from mp_game_engine import initialise_board, create_battleships, place_battleships, generate_attack
import tests.test_helper_functions as thf

testReport = thf.TestReport("test_report.txt")

def test_initialise_board_return_size():
    """
    Test if the initialise_board function returns a list of the correct size.
    """
    size = 10
    # Run the function
    board = initialise_board(size)
    # Check that the return is a list
    assert isinstance(board, list), "initialise_board function does not return a list"
    # check that the length of the list is the same as board
    assert len(board) == size, "initialise_board function does not return a list of the correct size"
    for row in board:
        # Check that each sub element is a list
        assert isinstance(row, list), "initialise_board function does not return a list of lists"
        # Check that each sub list is the same size as board
        assert len(row) == size, "initialise_board function does not return lists of the correct size"


def test_create_battleships_returns_dict():
    """
    Test if the create_battleships function returns a dictionary.
    """
    try:

        ships = create_battleships()

        assert isinstance(ships, dict)

    except AssertionError:
        testReport.add_message("create_battleships function does not return dictionary")
        pytest.fail("create_battleships function does not return dictionary")


def test_place_battleships_ships_placed():
    """
    Tests if the place_battleships function places all the ships properly.
    """
    try:
        board = initialise_board()
        ships = create_battleships()
        place_battleships(board, ships, 'random')
        for x in range(len(board)):
            for y in range(len(board)):

                if board[y][x] in ships:
                    ships.update({board[y][x]: (ships.get(board[y][x])-1)})
                    if ships.get(board[y][x]) == 0:
                        ships.pop(board[y][x])

        assert ships == {}

    except AssertionError:
        testReport.add_message("place_battleships function does not place all the ships on the board")
        pytest.fail("place_battleships function does not place all the ships on the board")

def test_place_battleships_random_hard_with_different_board_size():
    """
    Tests if the placement_battleships_random when run with algorithm 'Hard' can place ships
    in the correct areas for the algorithm for varying board sizes.
    """
    try:
        size = random.randint(10, 30)
        board = initialise_board(size)
        ships = create_battleships()
        place_battleships_random(board, ships, 'Hard')
        #Battleships greater than or equal to 4 should be in the outer 

        assert 0 <= coordinates[0] <= (size-1)
        try:
            assert 0 <= coordinates[1] <= (size-1)
        except AssertionError:
            testReport.add_message("generate_attack function does not generate valid y coordinate")
            pytest.fail("generate_attack function does not generate valid y coordinate")

    except AssertionError:
        testReport.add_message("generate_attack function does not generate valid x coordinate")
        pytest.fail("generate_attack function does not generate valid x coordinate")


def test_generate_attack_with_different_board_size():
    """
    Tests if the generate_attack function can generate valid coordinates for differing board sizes.
    """
    try:
        size = random.randint(10, 30)
        coordinates = generate_attack(size)

        assert 0 <= coordinates[0] <= (size-1)
        try:
            assert 0 <= coordinates[1] <= (size-1)
        except AssertionError:
            testReport.add_message("generate_attack function does not generate valid y coordinate")
            pytest.fail("generate_attack function does not generate valid y coordinate")

    except AssertionError:
        testReport.add_message("generate_attack function does not generate valid x coordinate")
        pytest.fail("generate_attack function does not generate valid x coordinate")