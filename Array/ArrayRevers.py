from Arrays import Array

def Revers(arr):
    start = arr[0]
    end =len(arr)
    while( start < end):
        arr[start],arr[end-1]= arr[end-1],arr[start]
        start +=1
        end-=1
    return arr

if __name__ == '__main__':
    arr = Array(10)
    for i in range(len(arr)):
        arr.insert(i*3,i)
    # print(len(arr))
    print('Arry before Reversing',arr)
    print("Resvered Array is:",Revers(arr))


