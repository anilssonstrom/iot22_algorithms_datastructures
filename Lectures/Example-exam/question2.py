def rotate_left(d, arr):
    """ Rotate the list "arr" left, by "d" steps. """

    while d >= 1:
        x = arr.pop(0)
        arr.append(x)
        d -= 1

    return arr


if __name__ == '__main__':
    assert rotate_left(2, [1, 2, 3, 4, 5]) == [3, 4, 5, 1, 2]
    assert rotate_left(1, [1, 2, 3, 4, 5]) == [2, 3, 4, 5, 1]

    a = [1, 2, 3, 4, 5]
    print(a, '->', rotate_left(2, a.copy()))

    print("Done!")
