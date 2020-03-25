def test_function(x):
    """
        Assume we enter a positive or at least non-negative x.
    """
    print('entering test function', x)
    if x == 0:
        return 1
    else:
        return test_function(x - 1)


# n! = n * (n - 1)!
def fact(x):
    if x == 0:  # base case
        return 1
    else:  # recursive case
        y = x * fact(x - 1)
        print(y)
        return y


def fact_loopy(x):
    total = 1
    # why didn't i just do range(x)? 0 ... (x - 1)
    for i in range(1, x + 1):
        total *= i

    return total


def fib(n):
    if n < 2:
        return 1
    else:
        print('calling fib', n - 1)
        x = fib(n - 1)
        print('calling fib', n - 2)
        y = fib(n - 2)
        return x + y


def fib_loops(n):
    fprev = 1
    fprevprev = 1
    current = 0
    if n < 2:
        return 1
    for i in range(n):
        current = fprev + fprevprev
        fprevprev = fprev
        fprev = current

    return current


def as_and_bs(length, partial):
    """
    :param length: length of as and bs left
    :param partial: current string to add more a's and b's to
    :return: none
    """
    if length <= 0:
        print(partial)
    else:
        as_and_bs(length - 1, partial + 'a')
        as_and_bs(length - 1, partial + 'b')


def recursive_palindrome(the_word):
    # silly way of saying if len(the_word) == 0 or len(the_word) == 1:
    if len(the_word) in [0, 1]:
        # consider all single letter words and the empty string ARE palindromes
        return True
    else:
        if the_word[0] == the_word[len(the_word) - 1]:
            # could still be a palindrome
            # slices return up to the last index, but not including it.
            print(the_word[1:len(the_word) - 1])
            return recursive_palindrome(the_word[1:len(the_word) - 1])
        else:
            # its not we found two letters that dont match
            return False


if __name__ == '__main__':
    # as_and_bs(8, '')

    # print(recursive_palindrome('tacocat'))
    # print(recursive_palindrome('pineappleelppaenip'))
    # print(recursive_palindrome('​oogaliegoogeilagoo'))
    # print(recursive_palindrome('asdfasdfasdfasdfasdfasd'))
    print(recursive_palindrome('tthatt'))
