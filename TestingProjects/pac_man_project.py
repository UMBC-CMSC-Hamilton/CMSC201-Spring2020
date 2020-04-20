"""
Everyone wants to know about testing.
"""


class PacMan:

    def __init__(self):
        self.the_board = []
        self.baddies = []
        print('Pac Man Constructor Running')

    def load_map(self, map_file):
        """
        :param map_file: file name as string
        :return: board, 2d list which is the grid
        """
        # not because you're actually going to set it equal to something, but you want this to be passed to the test functions.
        return self.the_board

    def take_turn(self, board):
        pass

    # we might not test this.
    def play_game(self):
        pass

    def move_baddies(self):
        pass

    def check_move(self, the_board, x, y):
        # call me a method
        pass


def blah_fun():
    # just a function
    pass

if __name__ == '__main__':
    p = PacMan()
    p.play_game()
