class Character:
    def __init__(self):
        self.position = (0, 0)
        # character stats are going to go here

    def create_character(self):
        pass

    def move(self):
        pass


class Grid:
    """
    _ = open
    S = start
    E = end
    P = player
    G = gremlin
    * = blocked
    """
    def __init__(self, grid_file_name):
        self.grid_array = []

    def load_grid_file(self, grid_file_name):
        pass

    def draw(self):
        pass

    def at(self, position):
        pass


class Gremlin:
    def __init__(self, starting_position, symbol):
        self.position = starting_position
        self.symbol = symbol

    def move(self):
        pass


# C++ case for class names
class TheGridGame:
    NUM_GREMLINS = 5

    def __init__(self, grid_file_name):
        self.the_grid = Grid(grid_file_name)
        self.player = Character()
        self.player.create_character()
        self.gremlins = []
        for i in range(self.NUM_GREMLINS):
            self.gremlins.append(Gremlin((2, 2), 'G'))

    def run(self):
        # is is for the end
        while self.the_grid.at(self.player.position) != 'E':
            self.the_grid.draw()
            self.player.move()
            for i in range(self.NUM_GREMLINS):
                self.gremlins[i].move()
            # check to see if gremlins ate the player.
            # lose condition


if __name__ == '__main__':
    grid_file_name = input('What grid file do you want? ')
    the_game = TheGridGame(grid_file_name)
    the_game.run()
