import random
import time


def time_test(sort1, sort2):
    num_tests = int(input('How many tests do you want to run? '))
    num_elements = int(input('How many elements do you want in each list? '))
    for i in range(num_tests):
        print('Test', i + 1)
        test_list = [random.randint(0, 100) for _ in range(num_elements)]
        copy_1 = list(test_list)
        copy_2 = list(test_list)
        print('\tSort 1 starting')
        time_start = time.perf_counter()
        sort1(copy_1)
        print('\tSort 1 completed in', time.perf_counter() - time_start)
        time_start = time.perf_counter()
        print('\tSort 2 starting')
        sort2(copy_2)
        print('\tSort 2 completed in', time.perf_counter() - time_start)

pod_racing = time_test


def swap(a_list, x, y):
    temp = a_list[x]
    a_list[x] = a_list[y]
    a_list[y] = temp


def bubble_sort(the_list):
    swapped = True
    # for j in range(len(the_list)):
    j = 0
    count = 0
    while swapped and j < len(the_list):
        # swapped = False
        for i in range(len(the_list) - 1):
            count += 1
            if the_list[i] > the_list[i + 1]:
                swap(the_list, i, i + 1)
                swapped = True
        j += 1
    # h'mutable
    print(count)
    return the_list


def selection_sort(the_list):
    # we need to search for the min from position the_list[i:]
    for i in range(len(the_list)):
        # implement a find-min operation
        #  the rest of the list from position 0 to i - 1 will already be sorted
        min_index = i
        for j in range(i + 1, len(the_list)):
            # what if the_min is a lie?
            if the_list[min_index] > the_list[j]:
                # replace it with the_list[j]
                min_index = j
            # do I need to check something? lazy solution == not to check
        if i != min_index:  # if we're not lazy
            swap(the_list, i, min_index)
    return the_list


def quick_sort(the_list):

    # print(the_list)
    if len(the_list) < 2:
        return the_list

    # plan of attack
    less_list = []
    equal_list = []
    greater_list = []

    jeff_the_pivot = the_list[0]

    for x in the_list:
        if x < jeff_the_pivot:
            less_list.append(x)
        elif x == jeff_the_pivot:
            equal_list.append(x)
        else:
            greater_list.append(x)

    return quick_sort(less_list) + equal_list + quick_sort(greater_list)


def linear_search(the_list, x):
    """
    :param the_list:
    :param x: is  x in the-list?
    :return: index if x in the list and -1 otherwise
    """
    for i in range(len(the_list)):
        if the_list[i] == x:
            return i
    return -1

# List must be sorted
# [ 1, 2, 5, 8, 9, 13, 17, 22] return whatever zorblax said
# [ 1, 2, 5, 8 ] return whatever she said
# [ 1, 2, 5, 8 ] return whatever he said
# [ 1, 2] yep, return True

def binary_search(the_list, x):
    pass


some_kind_of_list = [6, 9, 3, 2, 7, 3, 6, 23, 5, 4, 2, 1]
other_list = [1, 2, 3, 4, 5]

# we want this to be done by us now:
# some_kind_of_list.sort()
# print(selection_sort(some_kind_of_list))
# time_test(bubble_sort, selection_sort)

# print(quick_sort(some_kind_of_list))
pod_racing(selection_sort, quick_sort)
