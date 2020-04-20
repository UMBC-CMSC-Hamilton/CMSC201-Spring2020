# in pycharm you may see these red underscores.
from pac_man_project import PacMan


# this does work, even if it's red underscored


# you can play with this code, or you can write your tests as just functions as below:
class PacManTest(PacMan):
    # PacManTest is a child of PacMan
    def __init__(self):
        # whoever the parent of PacManTest, PacMan
        super().__init__()
        # runs the constructor of that parent.

    def test_load_map(self):
        print(self.load_map('you want a file, ill give you a file'))

    def test_play_game(self):
        pass

    def move_baddies(self):
        pass

    def test_take_turn(self):
        pass

    def test_check_move(self):
        pass


def test_load_map():
    # all your tests will eventually pass on your code
    p = PacMan()
    if p.load_map('test_board_1') == [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*'], ['B', '*', 'P']]:
        print('first board test passed')
    else:
        print('first board test failed')

    if p.load_map('test_board_2') == [['', '', ''], ['', '*', ''], ['', '*', ''], ['B', '*', 'P']]:
        print('first board test passed')
    else:
        print('first board test failed')


def test_move_baddies():
    # the_board, baddies
    p = PacMan()
    # change the variables inside of the PacMan
    p.the_board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*'], ['B', '*', 'P']]
    p.baddies = []

    new_positions = p.move_baddies()
    if new_positions == []:  # whatever the right answer is
        print('test passed')
    else:
        print('test failed')


pmt = PacManTest()
pmt.test_load_map()
