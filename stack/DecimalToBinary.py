import Stack
def DecToBinary(decimal):
    stck = Stack.Stack(100)
    while decimal>0:
        stck.push(decimal%2)
        decimal //=2
    result =''
    while not stck.isEmpty():
        result += str(stck.pop())
    return result
    

if __name__=="__main__":
    print(DecToBinary(19234))