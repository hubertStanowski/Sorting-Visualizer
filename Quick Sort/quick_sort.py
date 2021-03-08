def partition(array, p, r):
    q = p
    pivot = array[r]

    for j in range(p, r):

        if array[j] <= pivot:
            array[q], array[j] = array[j], array[q]
            q += 1

    array[q], array[r] = array[r], array[q]

    return q


def quick_sort(array, p, r):
    if len(array) < 2:
        return array
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)
        return array
