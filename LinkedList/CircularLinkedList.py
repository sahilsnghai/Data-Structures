class node:
    def __init__(self, data):
        self.data = data
        self.next = next


class createList:
    def __init__(self):
        self.head = node(None)
        self.tail = node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def add(self, data):
        newNode = node(data)
        if self.head.data is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head

    def display(self):
        current = self.head
        if self.head is None:
            print("List is Empty")
            return
        else:
            print(current.data)
            while (current.next != self.head):
                current = current.next
                print(current.data)
    
class circularList:
    c1 = createList()
    c1.add(1)
    c1.add(2)
    c1.add(3)
    c1.add(4)
    c1.add(5)
    c1.add(6)
    c1.add(7)
    c1.add(8)
    c1.display()
