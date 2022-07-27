from hashlib import new
from http.client import NETWORK_AUTHENTICATION_REQUIRED
from platform import release


class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublylist:
    def __init__(self):
        self.head = None

    def insertStart(self, data):
        newNode = node(data)
        if self.head == None:
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def insertEnd(self, data):
        newNode = node(data)
        temp = self.head
        
        while(temp.next != None):
            temp = temp.next
        # print(temp.prev.data,temp.data, temp.next)
        # print()
        # print(self.head.prev,self.head.data, self.head.next)
        temp.next = newNode
        newNode.prev = temp.prev

    def delete(self, data):
        temp = self.head
        if (temp.next != None):
            if (temp.data == data):
                temp.next.prev = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while(temp.next != None):
                    if (temp.data == data):
                        break
                    temp = temp.next
                if (temp.next):
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    temp.next = None
                    temp.prev = None
                else:
                    temp.prev.next = None
                    temp.prev = None
                return

        if(temp == None):
            return
    
    def printdll(self):
        temp = self.head 
        while(temp!=None):
            print(temp.data, end=' ')
            temp = temp.next

if __name__ == '__main__':
    dll = doublylist()
    dll.insertStart(1)
    dll.insertStart(2)
    dll.insertStart(3)
    dll.insertStart(4)
    dll.insertStart(5)
    dll.printdll()
    print()
    dll.insertEnd(6)
    dll.printdll()
    print()
    dll.delete(2)
    dll.printdll()