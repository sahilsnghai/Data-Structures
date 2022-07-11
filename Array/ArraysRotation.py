from Arrays import Array
# [1,2,3,4,5]
# [2,3,4,5,1]
# [3,4,5,1,2]
# [4,5,1,2,3]

def rotation(arr, rotateby):
    for i in range(0, rotateby):
        rotateOne(arr)
    return arr
def rotateOne(arr):
    for i in range(len(arr)-1):
        arr[i],arr[i+1] = arr[i+1],arr[i]

if __name__ == '__main__':
    arr = Array(5)
    for i in range(len(arr)):
        arr.insert(i+1, i)
    print(arr)
    print(f"Array before Rotation: {arr}")
    print("Array after Rotation: ", rotation(arr, 2))
