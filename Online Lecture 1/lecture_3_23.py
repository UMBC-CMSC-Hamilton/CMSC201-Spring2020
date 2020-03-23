"""
Lecture 3/23/2020

"""

# constants go right under the program's documentation
LOCATIONS = {'start': 'The Dorms', 'end': 'ITE'}


def sample_split():
    my_file = open('events.tx')
    my_lines = my_file.readlines()

    print(my_lines)
    for line in my_lines:
        print(line.split(','))


def add_thing_to_list(my_list):
    print(my_list)
    my_list.append(3)
    print(my_list)
    # we didn't return


def example_one():
    the_list = [1, 2, 5, 7, 9]
    add_thing_to_list(the_list)
    print(the_list)

    # key : value
    places = {'Eiffel Tower': 34, 'Manhattan': 77, 'Mexico': 28, 'Svalbard': 237}

    # for each style of loop, you're going to get the key not the value
    for p in places:
        # access the dictionary as if it was a list, with the key as the index
        print(p, places[p])

    print(places.keys())
    print(places.values())

    places['Manhattan'] = 92
    print(places)

    # second question, can a dictionary have more than one value per key.
    # also really helpful on the project
    places['Maryland'] = [1, 2, 5, 7]
    print(places)

    tricky_places = {"Manhattan": 77, "Manhattan": 92}
    print(tricky_places)


def example_two():
    new_list = [1, 3, 5]

    # big_list = [ new_list, new_list, new_list ]
    big_list = []
    for i in range(3):
        big_list.append(list(new_list))

    new_list[1] = 17

    print(big_list)


if __name__ == '__main__':
    example_two()
