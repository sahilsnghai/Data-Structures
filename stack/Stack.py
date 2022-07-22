class Stack(object):
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    def push(self, data):
        if len(self.stack) >= self.limit:
            print('Stack OverFlow')
        else:
            self.stack.append(data)

    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[len(self.stack)-1]

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    stck = Stack(5)
    stck.push(2)
    stck.push(4)
    stck.push(3)
    stck.push(6)
    stck.push(7)
    print(stck)
    print(stck.pop())
    print(stck.peek())
    print(stck.isEmpty())
