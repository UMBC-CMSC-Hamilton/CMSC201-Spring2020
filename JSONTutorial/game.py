from shield import Shield
from weapon import Weapon
from player import Player

import json


class NotDiabloGame:
    def __init__(self):

        self.the_player = None
        # all the possible weapons in the game
        self.weapons = {}
        # all the possible shields in the game
        self.shields = {}

    def save(self, file_name):
        # bad json.dumps(self.weapons)

        # save all the weapons, if the player has them or not.
        weapon_dict = {}
        for weapon in self.weapons:
            # weapon is just a string.
            # self.weapons[weapon] the weapon class that we want to read.
            print(self.weapons[weapon].jsonify())
            # make us a weapon dictionary of all the weapons we add together.
            weapon_dict.update(self.weapons[weapon].jsonify())

        shield_dict = {}
        for shield in self.shields:
            print(self.shields[shield].jsonify())
            shield_dict.update(self.shields[shield].jsonify())

        with open(file_name, 'w') as game_file:
            # everything in one dictionary
            file_save_dictionary = {'shields': shield_dict, 'weapons': weapon_dict}
            # save everything as one json file
            game_file.write(json.dumps(file_save_dictionary))
            # this closes the game_file at the end of this statement.

    def load(self, file_name):
        with open(file_name, 'r') as read_json:
            the_entire_file = read_json.read()
            the_entire_dict = json.loads(the_entire_file)

            for shield_name in the_entire_dict['shields']:
                the_shield_dict = the_entire_dict['shields'][shield_name]
                new_shield = Shield(shield_name, the_shield_dict['type'], the_shield_dict['size'],
                       the_shield_dict['weight'], the_shield_dict['strength'])
                #prevents double loads, same name overwriting
                if shield_name not in self.shields:
                    # shield_name is the string, new_shield is the Shield object!
                    self.shields[shield_name] = new_shield

            for weapon_name in the_entire_dict['weapons']:
                the_weapon_dict = the_entire_dict['weapons'][weapon_name]
                new_weapon = Weapon(weapon_name, the_weapon_dict['type'], the_weapon_dict['reach'],
                       the_weapon_dict['weight'], the_weapon_dict['strength'])

                #prevents double loads, same name overwriting
                if weapon_name not in self.weapons:
                    # shield_name is the string, new_shield is the Shield object!
                    self.weapons[weapon_name] = new_weapon

        print(self.weapons)
        print(self.shields)


    def test_loop(self):
        player_name = input('What is the player name: ')
        self.the_player = Player(player_name)

        in_string = input('What do you want to do next? ')
        while in_string.lower() not in ['quit', 'exit']:
            if in_string == 'create weapon':
                self.create_weapon()
            elif in_string == 'create shield':
                self.create_shield()
            elif in_string == 'add weapon to inventory':
                new_weapon = input('What weapon should we add? ')
                if new_weapon in self.weapons:
                    self.the_player.inventory.append(self.weapons[new_weapon])
            elif in_string == 'add shield to inventory':
                new_shield = input('What shield should we add? ')
                if new_shield in self.shields:
                    # because it's a dictionary we need:
                    # self.shields[new_shield]
                    # new_shield string name of the thing.
                    self.the_player.inventory.append(self.shields[new_shield])
            elif in_string == 'load file':
                file_name = input('What file name do you want to load? ')
                self.load(file_name)
            elif in_string == 'save file':
                file_name = input('What file name do you want to save as? ')
                self.save(file_name)

            in_string = input('What do you want to do next? ')

    def create_weapon(self):
        weapon_name = input('\tWhat is the name of the weapon we are creating? ')
        weapon_type = input('\tWhat is the type of the weapon we are creating? ')
        reach = int(input('\tWhat is the weapon reach? '))
        weight = int(input('\tWhat is the weapon weight? '))
        strength = int(input('\tWhat is the weapon strength? '))
        if weapon_name not in self.weapons:
            self.weapons[weapon_name] = Weapon(weapon_name, weapon_type, reach, weight, strength)
            print('\t The weapon %s has been created.' % weapon_name)

    def create_shield(self):
        shield_name = input('\tWhat is the name of the shield we are creating? ')
        shield_type = input('\tWhat is the type of the shield we are creating? ')
        size = int(input('\tWhat is the shield size? '))
        weight = int(input('\tWhat is the shield weight? '))
        strength = int(input('\tWhat is the shield strength? '))
        if shield_name not in self.shields:
            self.shields[shield_name] = Shield(shield_name, shield_type, size, weight, strength)
            print('\t The shield %s has been created.' % shield_name)


if __name__ == '__main__':
    ndg = NotDiabloGame()
    ndg.test_loop()
