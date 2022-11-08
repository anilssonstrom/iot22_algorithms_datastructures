import random


def randomlist(n):
    """ Create n random integers between 0 and 100.000 """
    return [random.randint(0, 100000) for _ in range(n)]


def bubble_sort(values: list):
    """ Sort a list of integers, from smallest to largets """

    arr = values[::]
    is_sorted = True
    end = len(arr)
    while is_sorted:
        is_sorted = False
        for i in range(1, end):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                is_sorted = True
        end -= 1
    return arr


def quicksort(values: list):
    """ Sort a list of integers, from smallest to largets """

    arr = values[::]
    if len(arr) <= 1:
        return arr
    values = [x for x in arr[1:] if x <= arr[0]]
    r = [x for x in arr[1:] if x > arr[0]]
    return quicksort(values) + arr[0:1] + quicksort(r)


if __name__ == '__main__':
    print("Running test...\n")

    # Timeit används för att mäta hur lång tid olika funktioner tar
    import timeit

    nums = randomlist(1000)  # Create list of 1000 random values
    times = 100

    # Kör tre funktioner, ta medeltiden av 100 körningar
    bubblesort_time = timeit.timeit(lambda: bubble_sort(nums), number=times)
    quicksort_time = timeit.timeit(lambda: quicksort(nums), number=times)
    pysorted_time = timeit.timeit(lambda: sorted(nums), number=times)

    print(f"Timing sorting of {len(nums)} elements, average of {times} times, using:")
    print(f"Bubblesort    : {bubblesort_time:.3}")
    print(f"Quicksort     : {quicksort_time:.3}")
    print(f"Python sorted : {pysorted_time:.3}")
