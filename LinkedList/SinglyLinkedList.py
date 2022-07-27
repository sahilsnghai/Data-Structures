class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def setdata(self, data):
        self.data = data

    def getdata(self, data):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next


class Linkedlist:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def insertBgning(self, data):
        if self.head == None:
            newNode = node(data)
            self.head = newNode
        else:
            newNode = node(data)
            newNode.next = self.head
            self.head = newNode

    def insertLast(self, data):
        newNode = node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode

    def insertBetwn(self, data, lastdata):
        temp = self.head
        if lastdata is None:
            self.insertLast(data)
        else:
            while temp:
                if(temp.next.data == lastdata):
                    break
                temp = temp.next
            if temp == None:
                self.insertLast(data)
                return f'Node {lastdata} found in the list. {data} is added to the last'
            else:
                newNode = node(data)
                newNode.next = temp.next.next
                temp.next = newNode

    def search(self, data):
        temp = self.head
        while (temp):
            if temp.data == data:
                return "Found"
            temp = temp.next
        return 'Not Found'


if __name__ == '__main__':
    lst = Linkedlist()
    lst.head = node(1)
    node2 = node(2)
    lst.head.setNext(node2)
    lst.insertBgning(3)
    # lst.insertBetwn(5, node2)
    # lst.insertBetwn(5,2)
    lst.insertLast(6)
    lst.insertBetwn(7,5)
    lst.printList()
