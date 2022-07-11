from Arrays import Array

def missingnumber(n,arr):
    n = n-1
    sumup = (n*(n+1))//2
    for i in range(n):
        sumup -= arr[i]
    return sumup

if __name__=="__main__":
    arr = Array(10)
    for i in range(len(arr)):
        arr.insert(i,i)
    arr.delete(9)
    print("Array before Finding: ",arr)
    print("Missing Number is: ",missingnumber(len(arr),arr))
    