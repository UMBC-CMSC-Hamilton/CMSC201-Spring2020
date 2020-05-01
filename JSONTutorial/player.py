class Player:
    def __init__(self, name):
        self.name = name
        self.strength = 0
        self.intelligence = 0
        self.charisma = 0

        # this is the most important part:
        self.inventory = []
