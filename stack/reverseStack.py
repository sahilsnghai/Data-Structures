import Stack

def reverse(string):
    stck = Stack.Stack(20)
    for i in range(len(string)):
        stck.push(string[i])
    
    result=''
    for i in range(len(string)):
        result += str(stck.pop())
    return result

if __name__=='__main__':
    print(reverse('Sahil Singhai'))