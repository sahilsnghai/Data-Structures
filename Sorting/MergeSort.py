def MergerSort(array):
    if len(array) < 2:
        return array
    mid = len(array)//2
    left = MergerSort(array[:mid])
    right = MergerSort(array[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) or j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result

import random 

array = [i for i in range(1, 9)]
random.shuffle(array)
print(MergerSort(array))
