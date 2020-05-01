class Weapon:
    def __init__(self, name, weapon_type, reach, weight, strength):
        self.name = name
        self.weapon_type = weapon_type
        # shadows built in range
        self.reach = reach
        self.weight = weight
        self.strength = strength

    def jsonify(self):
        # converted the member variables inside of the class into a a dictionary.
        return {self.name: {'type': self.weapon_type, 'reach': self.reach, 'weight': self.weight, 'strength': self.strength}}
