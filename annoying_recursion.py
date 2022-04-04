def annoying_factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 4 * annoying_factorial(3)
    elif n == 5:
        return 5 * annoying_factorial(4)
    elif n == 6:
        return 6 * annoying_factorial(5)
    else:
        return int(n) * annoying_factorial(n-1)

def annoying_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return annoying_fibonacci(3) + annoying_fibonacci(2)
    elif n == 5:
        return annoying_fibonacci(4) + annoying_fibonacci(3)
    elif n == 6:
        return annoying_fibonacci(5) + annoying_fibonacci(4)
    else:
        return annoying_fibonacci(n-1) + annoying_fibonacci(n-2)

def annoying_valley(n):
    if n == 0:
        return None
    elif n == 1:
        print('*')
    elif n == 2:
        print('./')
        print('*')
        print('.\\')
    elif n == 3:
        print('../')
        print('./')
        print('*')
        print('.\\')
        print('..\\')
    elif n == 4:
        print('.../')
        annoying_valley(3)
        print('...\\')
    elif n == 5:
        print('..../')
        annoying_valley(4)
        print('....\\')
    elif n == 6:
        print('...../')
        annoying_valley(5)
        print('.....\\')
    else:
        print('.' * (n-1) + '/')
        annoying_valley(n-1)
        print('.' * (n-1) + '\\')

def annoying_int_sequence(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2, 1]
    if n == 3:
        return [1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1]
    if n == 4:
        var_4 = annoying_int_sequence(3)
        return ((var_4 + [4])*4)[:-1]
    if n == 5:
        var_5 = annoying_int_sequence(4)
        return ((var_5 + [5])*5)[:-1]
    if n == 6:
        var_6 = annoying_int_sequence(5)
        return ((var_6 + [6])*6)[:-1]
    else:
        var_n = annoying_int_sequence(n-1)
        return ((var_n + [n])*n)[:-1]


