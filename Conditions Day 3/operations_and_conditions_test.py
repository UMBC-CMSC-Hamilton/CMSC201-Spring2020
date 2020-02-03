import sys
import re
import random

introduction_string = """
Welcome to the Operations and Conditions Testing Script
    Options are:
        monsters
        switches
        weekdays
"""


class MonsterTest:

    def __init__(self, test_path=''):
        self.filename = 'monsters.py'
        self.test_path = test_path
        self.test_globals = {'__name__': '__main__', '__builtins__': {'abs': abs, 'print': self.print, 'input': self.input, 'int': int, 'float': float, 'bool': bool, 'str': str, 'pow': pow}}
        self.results = {}
        self.current_output = []
        self.input_values = []
        self.test_number = 0

    def print(self, *args, **kwargs):
        if 'sep' not in kwargs:
            kwargs['sep'] = ' '
        if 'end' not in kwargs:
            kwargs['end'] = '\n'
        # print(args)

        if isinstance(args, tuple) or isinstance(args, list):
            self.current_output.append(kwargs['sep'].join([str(x) for x in args]) + kwargs['end'])
        elif isinstance(args, str):
            self.current_output.append(args + kwargs['end'])

    def input(self, prompt):
        if isinstance(prompt, str):
            self.in_count += 1
            if self.in_count < len(self.input_values):
                return self.input_values[self.in_count]
            else:
                return ''
        else:
            raise ValueError('Prompt in input statement must be a string.')

    def run_tests(self, num_tests=8):
        failed_tests = 0
        test_list = [['Megazord', '300', 'Godzilla', '1'], ['Killer Bees', '75', 'Arg-Monster', '750000'], ['A', '250', 'B', '6'], ['D', '0', 'C', '-2'], ['D', '0', 'D', '500']]
        for i, test in enumerate(test_list):
            self.test_number = i + 1
            self.current_output = []
            self.input_values = test
            self.in_count = -1
            failed_tests += 1 if not self.run_test(i) else 0
        print('Tests Passed: ', len(test_list) - failed_tests, 'out of', len(test_list))

    def run_test(self, test_day):
        self.current_day_number = test_day
        failed_tests = 0

        try:
            with open(self.filename) as test_file:
                test_code = test_file.read()
                temp_locals = {}
                try:
                    test_passed = False
                    exec(test_code, self.test_globals, temp_locals)
                    result = self.monster_result(self.input_values)

                    for line in self.current_output:
                        if result.lower() in line.lower():
                            test_passed = True

                    if not test_passed:
                        print('Test', self.test_number, 'failed', '\t\t(input: ', self.current_day_number, 'output:', result, ')')

                except Exception as exc:
                    print('Test: ', self.test_number, 'Exception Thrown', str(exc))
                    test_passed = False
        except OSError:
            print('File', self.filename, 'could not be found or opened.  ')
            test_passed = False
        return test_passed

    @staticmethod
    def monster_result(input_values):
        first_monster = input_values[0]
        first_monster_strength = int(input_values[1])

        second_monster = input_values[2]
        second_monster_strength = int(input_values[3])

        if first_monster == second_monster:
            return 'They are the same!'
        elif first_monster == 'Godzilla' or second_monster == 'Godzilla':
            return 'Godzilla wins'
        elif first_monster_strength >= second_monster_strength:
            return 'First monster wins'
        else:
            return 'Second monster wins'



class SwitchesTest:

    def __init__(self, test_path=''):
        self.filename = 'switches.py'
        self.test_path = test_path
        self.test_globals = {'__name__': '__main__', '__builtins__': {'abs': abs, 'print': self.print, 'input': self.input, 'int': int, 'float': float, 'bool': bool, 'str': str, 'pow': pow}}
        self.results = {}
        self.current_output = []
        self.input_values = []
        self.test_number = 0

    def print(self, *args, **kwargs):
        if 'sep' not in kwargs:
            kwargs['sep'] = ' '
        if 'end' not in kwargs:
            kwargs['end'] = '\n'

        if isinstance(args, tuple) or isinstance(args, list):
            self.current_output.append(kwargs['sep'].join([str(x) for x in args]) + kwargs['end'])
        elif isinstance(args, str):
            self.current_output.append(args + kwargs['end'])

    def input(self, prompt):
        if isinstance(prompt, str):
            self.in_count += 1
            if self.in_count < len(self.input_values):
                return self.input_values[self.in_count]
            else:
                return ''
        else:
            raise ValueError('Prompt in input statement must be a string.')

    def run_tests(self, num_tests=0):
        failed_tests = 0
        test_list = [['on', 'on', 'on'], ['on', 'off', 'on'], ['on', 'on', 'off'], ['on', 'off', 'off'], ['off', 'on', 'on'], ['off', 'on', 'off'], ['off', 'off', 'on'], ['off', 'off', 'off']]
        for i, test in enumerate(test_list):
            self.test_number = i + 1
            self.current_output = []
            self.input_values = test
            self.in_count = -1
            failed_tests += 1 if not self.run_test(i) else 0
        print('Tests Passed: ', len(test_list) - failed_tests, 'out of', len(test_list))

    def run_test(self, test_day):

        try:
            with open(self.filename) as test_file:
                test_code = test_file.read()
                temp_locals = {}
                try:
                    test_passed = False
                    exec(test_code, self.test_globals, temp_locals)
                    if self.input_values[0] == 'on' and (self.input_values[1] == 'on' or self.input_values[2] == 'on'):
                        result = 'opened'
                    else:
                        result = 'closed'
                    for line in self.current_output:
                        if result.lower() in line.lower():
                            test_passed = True

                    if not test_passed:
                        print('Test', self.test_number, 'failed', '\t\t(input: ', ' '.join(self.input_values), 'output:', result, ')')

                except Exception as exc:
                    print('Test: ', self.test_number, 'Exception Thrown', str(exc))
                    test_passed = False
        except OSError:
            print('File', self.filename, 'could not be found or opened.  ')
            test_passed = False
        return test_passed


class WeekdayTest:
    """
        Currently set up for days of February 2020
    """

    DAYS_OF_WEEK = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    def __init__(self, test_path=''):
        self.filename = 'weekdays.py'
        self.test_path = test_path
        self.test_globals = {'__name__': '__main__', '__builtins__': {'abs': abs, 'print': self.print, 'input': self.input, 'int': int, 'float': float, 'bool': bool, 'str': str, 'pow': pow}}
        self.results = {}
        self.current_output = []
        self.input_values = []
        self.current_day_number = 0
        self.test_number = 0

    def print(self, *args, **kwargs):
        if 'sep' not in kwargs:
            kwargs['sep'] = ' '
        if 'end' not in kwargs:
            kwargs['end'] = '\n'

        if isinstance(args, tuple) or isinstance(args, list):
            self.current_output.append(kwargs['sep'].join([str(x) for x in args]) + kwargs['end'])
        elif isinstance(args, str):
            self.current_output.append(args + kwargs['end'])

    def input(self, prompt):
        if isinstance(prompt, str):
            return str(self.current_day_number)
        else:
            raise ValueError('Prompt in input statement must be a string.')

    def run_tests(self, num_tests=29):
        failed_tests = 0
        test_list = [i + 1 for i in range(num_tests)]
        for i, test_day in enumerate(test_list):
            self.test_number = i + 1
            self.current_output = []
            failed_tests += 1 if not self.run_test(test_day) else 0
        print('Tests Passed: ', 29 - failed_tests)

    def run_test(self, test_day):
        self.current_day_number = test_day
        failed_tests = 0

        try:
            with open(self.filename) as test_file:
                test_code = test_file.read()
                temp_locals = {}
                try:
                    test_passed = False
                    exec(test_code, self.test_globals, temp_locals)
                    result = self.DAYS_OF_WEEK[(self.current_day_number - 1) % 7]

                    for line in self.current_output:
                        # pass if the correct day is in there.
                        if result.lower() in line.lower():
                            test_passed = True
                        # fails the test if another day is also in the output string
                        for day in self.DAYS_OF_WEEK:
                            if day != result and day.lower() in line.lower():
                                test_passed = False

                    if not test_passed:
                        print('Test', self.test_number, 'failed', '\t\t(input: ', self.current_day_number, 'output:', result, ')')

                except Exception as exc:
                    print('Test: ', self.test_number, 'Exception Thrown', str(exc))
                    test_passed = False
        except OSError:
            print('File', self.filename, 'could not be found or opened.  ')
            test_passed = False
        return test_passed


if __name__ == '__main__':
    print(introduction_string)
    if len(sys.argv) > 1:
        test_name = sys.argv[1]
    else:
        test_name = input('Enter the test name you want to run: ')
    if test_name == 'weekdays':
        weekday_test = WeekdayTest()
        weekday_test.run_tests()
    elif test_name == 'switches':
        switches_test = SwitchesTest()
        switches_test.run_tests()
    elif test_name == 'monsters':
        monster_test = MonsterTest()
        monster_test.run_tests()
