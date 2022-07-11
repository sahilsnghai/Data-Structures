class Queue(object):
    def __init__(self, limit=10):
        self.queue = [None for i in range(limit)]
        self.front = -1
        self.rear = -1
        self.limit = limit

    def __str__(self):
        if self.rear >= self.front:
            return ' '.join([str(self.queue[i]) for i in range(self.front, self.rear+1)])
        else:
            q1 = ' '.join([str(self.queue[i])
                          for i in range(self.front, self.limit)])
            q2 = ' '.join([str(self.queue[i])
                          for i in range(0, self.rear + 1)])
            return q1 + ' ' + q2

    def isEmpty(self):
        return self.front == -1

    def isfull(self):
        return (self.rear + 1) % self.limit == self.front

    def enqueue(self, data):
        if self.isfull():
            return f"Queue is full"
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear+1) % self.limit
            self.queue[self.rear] = data

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        elif(self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front+1) % self.limit


if __name__ == "__main__":
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)
    print(queue)
    queue.dequeue()
    queue.dequeue()
    print(queue)
