# return [name, properties]
# return {}
# done other things


class Character:
    # constructor for the Character class
    def __init__(self, name, charisma, stealth):
        self.charisma = charisma
        self.stealth = stealth
        self.name = name

    def hello(self):
        print('hello i am', self.name, 'my charisma is', self.charisma, 'and my stealth is', self.stealth)


def dont_do_this_on_our_project():
    c = Character('robert', 5, 5)
    c.hello()
    d = Character('bill', 2, 8)
    d.hello()
    e = Character('jill', 7, 3)
    e.hello()


class Student:
    # don't do this. Next time you'll see what the problem is
    here_be_a_variable = 3

    def __init__(self, name):
        self.name = name
        self.gpa = 4.0
        self.schedule = []
        self.favorite_pizza = 'pepperoni'

    def take_class(self, course_name):
        self.schedule.append(course_name)

    def print_schedule(self):
        print('your current schedule is')
        for course in self.schedule:
            print('\t', course)

    def print_all_things(self):
        print(self.name, self.gpa, self.favorite_pizza)
        self.print_schedule()


eric = Student('Eric')
eric.take_class('cmsc 201')
eric.take_class('cmsc 203')
eric.take_class('phil 101')
eric.take_class('phys 122')
print(eric.gpa, eric.name, eric.favorite_pizza)

eric.print_all_things()
# thing before dot, sticks into the function:
# Student.print_schedule(eric, ...)

derek = Student('Derek')
eric.here_be_a_variable = 5
print(derek.here_be_a_variable)
