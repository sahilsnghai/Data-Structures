class StackQueue:
    def __init__(self):
        self.stack = Stack()
        self.AlternateStack = Stack()

    def enqueue(self, item):
        while (not self.stack.is_empty()):
            self.AlternateStack.push((self.stack.pop()))
        self.AlternateStack.push(item)
        
        while(not self.AlternateStack.is_empty()):
            self.stack.push(self.AlternateStack.pop())


    def dequeue(self):
        return self.stack.pop()

    def __repr__(self):
        return repr(self.stack)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def __repr__(self):
        return str(self.items)


if __name__=='__main__':
    Queue = StackQueue()
    Queue.enqueue(1)
    Queue.enqueue(2)
    Queue.enqueue(3)
    Queue.enqueue(4)
    Queue.enqueue(5)
    Queue.enqueue(6)
    Queue.enqueue(7)
    Queue.enqueue(8)
    print(Queue)
    Queue.dequeue()
    Queue.dequeue()
    print(Queue)