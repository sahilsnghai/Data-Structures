def oddTime(arr):
    odd = 0
    for element in arr:
        odd = odd ^ element
        # print(odd)
    return odd

if __name__=='__main__':
    arr = [2,3,1,4,2,2,5,7,5,8,4,1,3,4,2]
    print(oddTime(arr))