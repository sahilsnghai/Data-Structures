import Stack

def isOperand(char):
    return (ord(char)>= ord('a') and ord(char) <= ord('z')) or ord(char)>= ord('A') and ord(char) <= ord('Z')


def precedence(char):
    if char=='+'or char=='-':
        return 1
    elif char=='*' or char=='/':
        return 2
    elif char == '^':
        return 3
    else:
        return -1

def InfixToPostfix(exp,stck):
    postfix = []
    for i in range(len(exp)):
        if(isOperand(exp[i])):
            postfix.append(exp[i])
        elif(exp[i]=="("):
            stck.push(exp[i])
        elif(exp[i]==")"):
            topOperator = stck.pop()
            while(not stck.isEmpty() and topOperator !='('):
                postfix.append(topOperator)
                topOperator = stck.pop()
        else:
            while(not stck.isEmpty())and( precedence(exp[i])<=precedence(stck.peek())):
                postfix.append(stck.pop())
            stck.push(exp[i])
    
    while (not stck.isEmpty()):
        postfix.append(stck.pop())
    return  ' '.join(postfix)

if __name__=='__main__':
    exp ="a+b*(c^d-e)^(f+g*h)-i"
    exp = [i for i in exp]
    print("Infix:"," ".join(exp))
    stck =Stack.Stack(len(exp))
    print('Postfix:',InfixToPostfix(exp,stck))