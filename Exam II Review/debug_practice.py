# 3 coding problems, 2 debugging problems
# d(lab) <= d(test) < d(hw)

"""
Want: Find the three greatest numbers in my_list, and return them in a separate list.
Just coding standard, then not an error.

Syntax error (breaks python)
Logic error (code doesn't work)
"""


def find_three_max_buggy(my_list):
    """
        my_list is a parameter which is a list
        this function will return the three greatest elements from a list, or however many elements if its <= 3.
        what i want on the exam
    """
    three_most = []
    for x in my_list:
        if len(three_most) < 3:  # changed <= to just < because it will include 4 or more
            three_most.append(x)
        else:  # [4, 4, 4] x = 4
            min_index = 0
            for i in range(3):  # comment all this stuff,
                if three_most[i] < three_most[min_index]:  # need to replace the min index,
                    # if you don't then it could replace the middle or even the max, cause strangeness
                    min_index = i

            if x > three_most[min_index]:  # if the element at the min index is too small, replace it.
                three_most[min_index] = x

    # print(three_most) line prints instead of returns
    return sorted(three_most)  # don't have to explain this, already done above.


def test_find_three_max():
    """
    This part is not for the exam, but is for the project.
    """
    # one test.  give some input to our function we want to test
    # run the function, and check the return, output
    result = find_three_max_buggy([1, 2, 3])
    if [1, 2, 3] == result and len(result) == 3:
        print('test 1 passed')
    else:
        print('test 1 failed, output was', result)

    result = find_three_max_buggy([4, 3, 2, 1])
    if 4 in result and 3 in result and 2 in result and len(result) == 3:
        print('test 2 passed')
    else:
        print('test 2 failed, output was', result)

    result = find_three_max_buggy([1, 2, 3, 4, 5, 6])
    if 4 in result and 5 in result and 6 in result and len(result) == 3:
        print('test 3 passed')
    else:
        print('test 3 failed, output was', result)


def is_prime_buggy(n):
    if -1 <= n <= 1:
        return False  # a-ok no problem

    for k in range(2, n):  # zero was bad, but we dont' want to mod by 1 either.  n/ 1 = n R 0
        if n % k == 0:  # always zero if you use k = 1
            return False  # if it is divisible you want to return False

    return True  # it never got divided by anything less than it.


def test_is_prime():
    # goal needs to be: generate tests that span as many possibilties as you can think of.
    # you should know the answer... don't make the problem so hard that you don't know the answer to the test
    # tests should be as simple as possible to test a single functional aspect, or logical path

    if is_prime_buggy(1) == False:
        print('test passed')
    else:
        print('test 1 failed, one is not prime')

    if is_prime_buggy(2) == True:
        print('test passed')
    else:
        print('test 2 failed, two is prime')

    if is_prime_buggy(9) == False:
        print('test passed')
    else:
        print('test 3 failed, nine is not prime')

    if is_prime_buggy(17) == True:
        print('test passed')
    else:
        print('test 4 failed, 17 is prime')

    if is_prime_buggy(125) == False:
        print('test passed')
    else:
        print('test 4.1 failed, 125 is not prime')

    # not a prime, not a prime to a power, just some rando number that is definitely not prime. 48 = 12 * 4 = 4 * 4 * 3 = 2^4 * 3
    if is_prime_buggy(48) == False:
        print('test passed')
    else:
        print('test 4.2 failed, 48 is not prime')

    # extreme test decent
    if is_prime_buggy(16127) == True:
        print('test passed')
    else:
        print('test 5 failed, 16127 ? is prime')


test_is_prime()

# test_find_three_max()
