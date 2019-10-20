import numpy as np

def init_board():
    """Creates the tic tac toe board

    Returns
    -------
    np.array
    """
    return np.full((3, 3), ' ')

def show_board(board):
    """Return string that visualizes the board

    Parameters
    ----------
    board : np.arrray
        Numpy array representing the board

    Returns
    -------
    str
    """
    output = ''
    first_line = True
    for line in board:
        first_element = True
        if first_line:
            for element in line:
                if first_element:
                    first_element = False
                    output += f'{element}'
                else:
                    output += f'|{element}'
            first_line = False
        else:
            output += '\n-----\n'
            for element in line:
                if first_element:
                    first_element = False
                    output += f'{element}'
                else:
                    output += f'|{element}'
    return output

def row_equal(row):
    """Checks if all values in a list are the same

    Parameters
    ----------
    row : list
        Sequence of 3 within tic tac toe board

    Returns
    -------
    bool
        True is the list is the same

    """
    if len(set(row)) == 1 and ' ' not in row:
        return True

def check_winner(board):
    for row in board:
        if row_equal(row):
            return row[0]
    for column in board.T:
        if row_equal(column):
            return column[0]
    if row_equal(np.diag(board)):
        return np.diag(board)[0]
    if row_equal(np.diag(np.fliplr(board))):
        return np.diag(np.fliplr(board))[0]
    return None

def available_moves(board):
    """List available moves

    Parameters
    ----------
    board : np.array
        Tic Tac Toe board

    Returns
    -------
    list
        List of potential spots

    """
    return np.argwhere(board == ' ')
