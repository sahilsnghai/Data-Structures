import random
def InsertionSort(array):
    iteration = 0
    for i in range(1, len(array)):
        curr_value = array[i]
        for j in range(i-1, -1, -1):
            iteration += 1
            if array[j] < curr_value:
                array[j], array[j+1] = array[j+1], array[j]
            else:
                array[j+1] = curr_value
                break
    return iteration


array = [i for i in range(30)]
random.shuffle(array)
InsertionSort(array)
print(array)
print(InsertionSort(array))
