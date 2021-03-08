def merge(array, p, q, r):
    end_1 = q - p + 1
    end_2 = r - q
    half_1 = []
    half_2 = []

    for i in range(end_1):
        half_1.append(array[p + i])

    for j in range(end_2):
        half_2.append(array[q + 1 + j])

    i = 0
    j = 0
    k = p

    while i < len(half_1) and j < len(half_2):
        if half_1[i] <= half_2[j]:
            array[k] = half_1[i]
            i += 1
        else:
            array[k] = half_2[j]
            j += 1
        k += 1

    while i < len(half_1):
        array[k] = half_1[i]
        i += 1
        k += 1

    while j < len(half_2):
        array[k] = half_2[j]
        j += 1
        k += 1

    return array


def merge_sort(array, p, r):
    if p < r:
        q = (p+r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        return merge(array, p, q, r)