import random
def bubble_sort(array):
    n = len(array)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def Optimized_bubble_sort(array):
    iteration = 0
    for i in range(len(array)-1):
        swapped = False
        for j in range(len(array)-1):
            iteration += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    return iteration


array = [2, 4, 5, 3, 1, 6, 7, 8, 9]
array = [i for i in range(1,20)]
random.shuffle(array)

# bubble_sort(array)
print(array)
Optimized_bubble_sort(array)
print(array)
print(Optimized_bubble_sort(array))
