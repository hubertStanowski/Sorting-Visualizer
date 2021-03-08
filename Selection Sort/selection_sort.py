def swap(idx_1, idx_2, array):
    array[idx_1], array[idx_2] = array[idx_2], array[idx_1]


def find_min_idx(start_idx, array):
    min_idx = start_idx
    for i in range(start_idx+1, len(array)):
        if array[min_idx] > array[i]:
            min_idx = i

    return min_idx


def sort(array):
    for i in range(len(array)):
        min_idx = find_min_idx(i, array)
        swap(i, min_idx, array)

    return array
