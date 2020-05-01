class Shield:
    def __init__(self, name, shield_type, size, weight, strength):
        self.name = name
        # dont want to use type()
        self.shield_type = shield_type
        self.weight = weight
        self.size = size
        self.strength = strength

    def jsonify(self):
        # converted the member variables inside of the class into a a dictionary.
        # return [self.name, self.shield_type, self.size, self.weight, self.strength]
        return {self.name: {'type': self.shield_type, 'size': self.size, 'weight': self.weight, 'strength': self.strength}}
