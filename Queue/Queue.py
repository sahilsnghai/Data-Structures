class Queue(object):
    def __init__(self, limit=10):
        self.queue = []
        self.front = None
        self.rear = None
        self.limit = limit
        self.size = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return self.size <= 0

    def enqueue(self, data):
        if self.size >= self.limit:
            return f"Queue is full"
        else:
            self.queue.append(data)
        self.size += 1

        if self.front is None:
            self.front = self.rear = 0
        else:
            self.front = self.queue[0]
            self.rear = self.size

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            poped = self.queue.pop(queue.front)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = 0

            else:
                self.front = self.queue[0]
                self.rear = self.queue[self.size-1]
        return poped

    def getSize(self):
        return self.size


if __name__ == "__main__":
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)
    print("Queue: ", queue)
    print("front after dequeue: ", queue.front)
    print("front after dequeue: ", queue.rear)
    print("Dequeue: ", queue.dequeue())
    print("front after dequeue: ", queue.front)
    print("rear after dequeue: ", queue.rear)
