class Queue(object):
    def __init__(self, limit=10):
        self.queue = []
        self.limit = limit

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) <= 0

    def isFull(self):
        return len(self.queue) >= 0

    def insertFront(self, data):
        if len(self.queue) >= self.limit:
            return f"Queue is full"
        else:
            self.queue.append(data)

    def insertLast(self, data):
        if len(self.queue) >= self.limit:
            return f"Queue is full"
        else:
            self.queue.insert(0, data)
        # self.front = self.queue(self.size -1)
        # self.rear = self.queue(0)

    def deleteFront(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue.pop()

    def deleteRear(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue.pop(0)

    def getSize(self):
        return len(self.queue)


if __name__ == "__main__":
    queue = Queue()
    for i in range(10):
        queue.insertLast(i)
    print("Is full:", queue.isFull())
    print("isempty:", queue.isEmpty())
    print("Queue: ", queue)
    print("Size: ", queue.getSize())
    # print("front after deletion: ", queue.front)
    # print("front after deletion: ", queue.rear)
    print("deleteFront: ", queue.deleteFront(), '<-')
    # print("front after deleteFront: ", queue.front)
    # print("rear after deleteFront: ", queue.rear)
    print("deleteFront: ", queue.deleteFront(), '<-')
    print("Queue: ", queue)
    print("Size: ", queue.getSize())
    print("Queue: ", queue)
    print("deleteRear: ", queue.deleteRear())
    queue.insertLast(10)
    print("insertLast: ->", queue)
    queue.insertFront(11)
    print("insertFront: ", queue, "<-")
    # print("akdba: ",queue.rear)
