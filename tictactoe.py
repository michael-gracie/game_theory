import numpy as np

def show_board(board):
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
    return np.argwhere(board == ' ')
