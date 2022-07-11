class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) <= 0

    def isFull(self):
        return len(self.queue) >= 0
        
    def enqueue(self, data):
        self.queue.append(data)
        return "Successfully Inserted data"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            maxx = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[maxx]:
                    maxx = i
            item = self.queue[maxx]
            del self.queue[maxx]
            return item
                
        #     del self.queue[maxx]
        # return item 

if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.enqueue(12)
    myQueue.enqueue(1)
    myQueue.enqueue(14)
    myQueue.enqueue(7)
    print(myQueue)                # 12 1 14 7
    while not myQueue.isEmpty():
        print(myQueue.dequeue(), end = ' ')    # 14 12 7 1
