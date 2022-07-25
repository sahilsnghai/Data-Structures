global predecessor, successor
predecessor, successor =None ,None
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = node(data)
                return True

    def findPredecessorSuccessor(self, data,predecessor=None,successor = None):
        if self is None:
            return
        if self.data == data:
            if self.left is not None:
                temp = self.left
                if temp.right is not None:
                    while(temp.right):
                        temp = temp.right
                predecessor = temp
           
            if self.right is not None:
                temp = self.right
                if temp.right is not None:
                    while(temp.left):
                        temp = temp.left
                successor = temp
            return
        if data<self.data:
            print('left')
            self.left.findPredecessorSuccessor(data,predecessor, successor)
        else:
            print('right')
            self.right.findPredecessorSuccessor(data, predecessor ,successor)

if __name__ == '__main__':
    root = node(50)
    root.insert(30)
    root.insert(20)
    root.insert(40)
    root.insert(70)
    root.insert(60)
    root.insert(80)

    root.findPredecessorSuccessor(80)
    if  (predecessor is not None) and (successor is not None):
        print('Predecessor:', predecessor.data, 'Successor:', successor.data)
    else:
        print('Predecessor:', predecessor, 'Successor:', successor)
