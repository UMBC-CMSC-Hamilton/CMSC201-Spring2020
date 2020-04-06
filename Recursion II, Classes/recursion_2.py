def count_the_letter(string, letter):
    if not string:
        return 0
    elif letter == string[0]:
        return 1 + count_the_letter(string[1:], letter)
    else:
        return count_the_letter(string[1:], letter)


def recursive_factoring(x):
    if x == 1:
        return []
    else:
        for i in range(2, x + 1):
            if x % i == 0:
                return [i] + recursive_factoring(x // i)


# print(recursive_factoring(int(input('integer! '))))
print(count_the_letter(input('word! '), 'a'))
