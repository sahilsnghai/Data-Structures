def SelectionSort(array):
    iteration = 0
    for i in range(len(array)):
        mini = i
        for j in range(i+1, len(array)):
            iteration +=1
            if array[mini] > array[j]:
                mini = j
        if mini != i:
            array[i], array[mini] = array[mini], array[i]
    return iteration


import random
array =[i for i in range(20)]
random.shuffle(array)
print(array)
SelectionSort(array)
print(array)
print(SelectionSort(array))