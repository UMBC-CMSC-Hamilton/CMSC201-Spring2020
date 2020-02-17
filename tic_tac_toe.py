
def has_winner(board):
    """
    :param board: a 3x3 list of lists containing x's and o's.
    :return: 'x', 'o' for winners, 't' for tie, or '' if no winner
    """

    # scan rows and columns and diagonals
    diag = board[0][0]
    anti_diag = board[0][2]

    for i in range(3):
        if board[i][i] != diag:
            diag = ''
        if board[i][2-i] != anti_diag:
            anti_diag = ''

    if diag.lower() in ['x', 'o']:
        return diag
    if anti_diag.lower() in ['x', 'o']:
        return anti_diag

    filled = 0

    for i in range(3):
        current_row = board[i][0]
        current_col = board[0][i]
        for j in range(3):
            if board[i][j].lower() in ['x', 'o']:
                filled += 1

            if board[i][j].lower() not in ['x', 'o']:
                current_row = ''
            elif board[i][j].lower() != board[i][0].lower():
                current_row = ''

            if board[j][i].lower() not in ['x', 'o']:
                current_col = ''
            elif board[j][i].lower() != board[0][i].lower():
                current_col = ''
        if current_col:
            return current_col
        if current_row:
            return current_row

    if filled == 9:
        return 't'
    return ''


def print_board(board):
    """
    :param board: takes a 3x3 list of lists defining a tic-tac-toe board
    :return: prints it out in a very minimalistic way.
    """
    for row in board:
        print('|'.join(row))
        print('-' * 6)
