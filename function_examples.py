def capitalize(my_string):
    capitalized = my_string[0].upper()
    for i in range(1, len(my_string)):
        capitalized += my_string[i]
    
    return capitalized


def even_or_odd(x):
    if x % 2:
        return 'odd'
    else:
        return 'even'


def is_friendly(x):
    the_sum = 0
    for i in range(1, x):
        if not x % i:
            the_sum += i
    
    if the_sum == x:
        return True
    
    return False


def blah_function():
    for i in range(0, 1000000):
        if is_friendly(i):
            print(i)


def is_prime(x, prime_list):
    for p in prime_list:
        if x % p == 0:
            return False
    
    return True


def get_primes():
    prime_list = [2]
    for x in range(3, 1000000):
        if is_prime(x, prime_list):
            prime_list.append(x)
    return prime_list


the_list = ['stuff', 'in', 'it']
blah_function()
print(the_list)
