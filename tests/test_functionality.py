import pytest
from game_engine import cli_coordinates_input, initialise_board, create_battleships
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
        pytest.TestReport.add_message("create_battleships function does not return dictionary")
        pytest.fail("create_battleships function does not return dictionary")


def test_create_battleships_dict_key_str_and_val_int():
    """
    Test if the create_battleships function's dictionary has a str key and int value.
    """
    try:

        ships = create_battleships()

        assert isinstance(list(ships.keys())[0], type('str'))

        try:
            assert isinstance(list(ships.values())[0], type('int'))

        except AssertionError:
            pytest.TestReport.add_message("create_battleships function dictionary doesn't have int values")
            pytest.fail("create_battleships function dictionary doesn't have int values")

    except AssertionError:
        pytest.TestReport.add_message("create_battleships function dictionary doesn't have str keys")
        pytest.fail("create_battleships function dictionary doesn't have a str key")


def test_cli_coordinates_input_is_tuple(monkeypatch):
    """
    Test if the cli_coordinates_input function returns a tuple x,y.
    """
    try:
        inputs = iter(['5','6'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        coordinates = cli_coordinates_input()

        assert isinstance(coordinates, tuple)

    except AssertionError:
        pytest.TestReport.add_message("cli_coordinates_input function does not return a tuple")
        pytest.fail("cli_coordinates_input function does not return a tuple")

def test_cli_coordinates_x_and_y_are_int(monkeypatch):
    """
    Test if the cli_coordinates_input function return of a tuple (x, y) are both integers.
    """
    try:
        inputs = iter(['1','10'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        coordinates = cli_coordinates_input()

        assert isinstance(coordinates[0], int)

        try:
            assert isinstance(coordinates[1], int)

        except AssertionError:
            pytest.TestReport.add_message("cli_coordinates_input function does not return integers for y")
            pytest.fail("cli_coordinates_input function does not return integers for y")

    except AssertionError:
        pytest.TestReport.add_message("cli_coordinates_input function does not return integers for x")
        pytest.fail("cli_coordinates_input function does not return integers for x")