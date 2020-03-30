# 2d list is a list within a list.

def my_first_2d_list_example():
    my_first_2d_list = [[1, 2, 3], [3, 4, 5]]

    print(my_first_2d_list[0])
    print(my_first_2d_list[1])
    print(my_first_2d_list[0][0])  # 1
    print(my_first_2d_list[1][1])  # 4
    print(my_first_2d_list[0][2])  # 3


def weird_indexing():
    # first index, call that rows
    # second index, call that columns
    new_list = [[1, 4, 6, 2], [3, 6, 28, 1], [42, 6, 13, 8], [51, 2, 33, 4]]
    print(new_list[3][2])  # 33
    print(new_list[1][3])  # 1
    print(new_list[2][2])  # 13
    print(new_list[0][3])  # 2


def lists_with_sublists_of_different_sizes():
    weird_list = [[1, 2, 3], [2, 4, 6, 8, 10], [1, 2, 3, 4, 5, 6, 7], [1, 1, 1], [2, 2, 2, 2]]
    print(weird_list)
    print('here are the individual lists')
    # for test_list in weird_list:
    #    print(test_list)

    # more general formulation, in case you need indices.
    for i in range(len(weird_list)):  # out list index, row index
        for j in range(len(weird_list[i])):  # inner list index, col index, sublist index
            print(weird_list[i][j], end=" . ")
        print()


def determinant_2(matrix):
    """
    :param matrix: must be a 2x2 list of lists.
    :return: the determinant
    """
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def tic_tac_toe(board):
    """
    :param board: 3x3 list of lists.  (2d-list) 'x' for x's , 'o' for o's and '' for nothing yet
    :return: 'x' if 'x' is the winner, 'o' if 'o' is the winner, 't' if board filled, but no winner,
            and '' if board not filled and no winner
    """
    # rows first
    for row in range(len(board)):
        current = board[row][0]
        # if the current string is not empty, it is going to be x or o:
        if current:
            for col in range(len(board[row])):
                if board[row][col] != current:
                    current = ''
            if current:  # != '', current is the winner if not empty
                return current
    # done the columns, same as rows basically
    for col in range(len(board[0])):
        current = board[0][col]
        # if the current string is not empty, it is going to be x or o:
        if current:
            for row in range(len(board)):
                if board[row][col] != current:
                    current = ''
            if current:  # != '', current is the winner if not empty
                return current

    diag = board[0][0]
    anti_diag = board[0][2]
    for i in range(len(board)):
        if board[i][i] != diag:
            diag = ''
        # (i, 2 - i) what is this doing?
        if board[i][2 - i] != anti_diag:
            anti_diag = ''

    if diag:
        return diag
    if anti_diag:
        return anti_diag
    # no winner
    return ''


def test_tic_tac_toe():
    if tic_tac_toe([['x', 'x', 'x'], ['', '', 'o'], ['', 'o', '']]) == 'x':
        print('row test passed', tic_tac_toe([['x', 'x', 'x'], ['', '', 'o'], ['', 'o', '']]))
    else:
        print('row test failed', tic_tac_toe([['x', 'x', 'x'], ['', '', 'o'], ['', 'o', '']]))

    if tic_tac_toe([['', '', 'x'],
                    ['o', 'x', 'o'],
                    ['x', 'o', 'o']]) == 'x':
        print('anti-diagonal passed')
    else:
        print('anti-diagonal failed')

    if tic_tac_toe([['o', '', 'x'],
                    ['o', 'o', 'x'],
                    ['x', 'o', 'o']]) == 'o':
        print('diagonal passed')
    else:
        print('diagonal failed')

    if tic_tac_toe([['x', 'o', 'x'],
                    ['o', 'o', 'x'],
                    ['x', 'o', 'o']]) == 'o':
        print('column test passed')
    else:
        print('column test failed')


def maze_walking(maze):
    """
     can't modify the maze, because strings are immutable.
    :param maze:
    :return:
    """
    position_x = 0
    position_y = 0
    while maze[position_x][position_y] != 'G':
        for i in range(len(maze)):
            if position_x == i:
                # slice goes up until position_y, but doesn't include, [position_y:] goes until the end of the row
                print(maze[position_x][0:position_y] + 'P' + maze[position_x][position_y + 1:])
            else:
                print(maze[i])
        wasd = input('Enter wasd: ').lower()
        if position_x > 0 and wasd == 'w' and maze[position_x - 1][position_y] != '*':
            position_x -= 1
        elif position_x < len(maze) - 1 and wasd == 's' and maze[position_x + 1][position_y] != '*':
            position_x += 1
        elif position_y > 0 and wasd == 'a' and maze[position_x][position_y - 1] != '*':
            position_y -= 1
        elif position_y < len(maze[position_x]) - 1 and wasd == 'd' and maze[position_x][position_y + 1] != '*':
            position_y += 1


# weird_indexing()
# lists_with_sublists_of_different_sizes()
# print(determinant_2([[1, 1], [0, 1]]))
# print(determinant_2([[13, 7], [-2, 5]]))
# print(determinant_2([[13, 7], [26, 14]]))
# test_tic_tac_toe()
# G is the goal
# * is a forbidden position
# '_' is a regular position
# maze = ['_____', '*____', '*_*__', '*G***']
# maze_walking(maze)

my_favorite_string = 'enqueueing'
print(my_favorite_string[3])
# my_favorite_string[3] = 't'
# print(my_favorite_string)
# pretty gross right?
# my_other_string = my_favorite_string[0:3] + 't' + my_favorite_string[4:]
# print(my_other_string)

# future life, currently forbidden arts, replaces both u's so actually not quite what we want anyway
my_favorite_string = my_favorite_string.replace('u', 't', 1)
# my_favorite_string is truly immutable
print(my_favorite_string)
