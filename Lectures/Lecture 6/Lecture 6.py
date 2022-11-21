
# Fakultet (factorial)

def factorial(n):
    """ Räkna ut n-fakultet (n!) """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def sum_list(lst):
    """ Summera alla tal i en lista """
    # [5, 4, 2, 7, 1]
    # 5 + [4, 2, 7, 1]
    # 5 + 4 + [2, 7, 1]

    if len(lst) == 1:
        return lst[0]  # Basfall
    else:
        return lst[0] + sum_list(lst[1:])  # Rekursiva fallet


def power(n, p):
    """ Räkna ut n ^ p """
    if p == 0:  # basfall
        return 1
    else:  # Rekursivt fall
        return n * power(n, p-1)


if __name__ == '__main__':
    # print(factorial(10))  # 10 * 9 * 8 * ... * 2 * 1
    # print(sum_list([5]))
    # print(sum_list([2, 5]))
    # print(sum_list([5, 4, 2, 7, 1]))
    # print(power(4, 3))  # 4 * 4 * 4

    print(power(4, 0))  # == 1
    print(power(4, 1))  # == 4  ( 4 * 1 )
    print(power(4, 2))  # power(4, 2) * power(4, 1) * power(4, 0)
    print(power(4, 6))  # 4096
