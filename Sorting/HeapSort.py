def heapify(array, heap_size, root_index):
    largest = root_index
    leftchild = (2*root_index)+1
    rightchild = (2*root_index)+2

    if leftchild < heap_size and array[leftchild] > array[largest]:
        largest = leftchild

    if rightchild < heap_size and array[rightchild] > array[largest]:
        largest = rightchild

    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        heapify(array, heap_size, largest)


def heap_sort(array):
    n = len(array)
    
    for i in range(n, -1, -1):
        heapify(array, n, i)
    
    for i in range(n-1,0,-1):
        array[i],array[0] = array[0],array[i]
        heapify(array,i,0)


array = [35, 12, 43, 8, 51, 23]
heap_sort(array)
print(array)
