from random import shuffle
def partition(array, start,end):
    i = start -1
    pivot =array[end]
    for j in range(start,end):
        if array[j] <pivot:
            i+=1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[end] = array[end],array[i+1]
    return i+1

def quick_sort(array,start,end):
    if start < end:
        temp = partition(array,start, end)
        quick_sort(array, start, temp-1)
        quick_sort(array,temp,end)


array = [i for i in range(1,6)]
# array.sort( reverse=True)
shuffle(array)
print(array)

quick_sort(array,0,len(array)-1)
print(array)