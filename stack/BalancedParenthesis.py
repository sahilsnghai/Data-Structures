import Stack


def parseParenthesis(string):
    balance = 1
    indx = 0
    stck = Stack.Stack(len(string))#4
    while(indx < len(string)) and (balance == 1):
        check = string[indx]#( ) ) ( ( )
        if check == '(':
            stck.push(check) #check =( 
        else:
            if stck.isEmpty(): 
                balance = 0
            else:
                stck.pop()
        indx += 1

    if balance == 1 and stck.isEmpty():
        return True
    else:
        return False


if __name__ == '__main__':
    print(parseParenthesis("()()"))
    print(parseParenthesis("(())"))
    print(parseParenthesis("())(()"))
# | |
# | |
# | |
# | |
# | |
# | |
# ___
