def checksum(arr, summ):
    arr = sorted(arr)
    leftind = 0
    rightind = len(arr)-1
    while leftind <= rightind:
        if (arr[leftind] + arr[rightind] == summ):
            return arr[leftind], arr[rightind]
        elif (arr[leftind] + arr[rightind] < summ):
            leftind += 1
        else:
            rightind -= 1
    return False, False


if __name__ == '__main__':
    arr = [11, 20, 30, 40, 50,2]
    # print(sorted(arr))
    summ = 60
    num1, num2 = checksum(arr, summ)

    if(num1 and num2):
        print(f"Sum of {num1} and {num2} is equal to {summ}")
    else:
        print(f"Array does not have Elements with {sum}")
