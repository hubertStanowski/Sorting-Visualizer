import random


def partition(array, p, r):
    q = p + 1
    pivot = array[p]
    for j in range(p + 1, r + 1):

        if array[j] <= pivot:
            array[q], array[j] = array[j], array[q]
            q += 1

    array[q - 1], array[p] = array[p], array[q - 1]

    return q - 1


def random_partition(array, p, r):
    pivot = random.randrange(p, r)
    array[p], array[pivot] = array[pivot], array[p]
    return partition(array, p, r)


def quick_sort(array, p, r):
    if len(array) < 2:
        return array
        
    if p < r:
        q = random_partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)
        return array