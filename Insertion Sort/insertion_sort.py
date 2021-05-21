def insert(idx, array):
    current = array[idx]
    prev_idx = idx - 1
    while prev_idx >= 0 and current < array[prev_idx]:
        slide_to_left(idx, array)
        prev_idx -= 1
        idx -= 1


def slide_to_left(idx, array):
    if idx > 0:
        array[idx - 1], array[idx] = array[idx], array[idx - 1]


def sort(array):
    for i in range(1, len(array)):
        insert(i, array)

    return array