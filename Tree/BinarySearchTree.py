class node:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild = node(data)
                return True
        else:
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild = node(data)
                return True

    def minValnode(self, node):
        current = node

        while(current.leftchild is not None):
            current = current.leftchild
        return current

    def maxValnode(self, node):
        current = node
        while(current.rightchild is not None):
            current = current.rightchild
        return current

    def delete(self, data, root):

        if self is None:
            return None

        if data < self.data:
            self.leftchild = self.leftchild.delete(data, root)
        elif data > self.data:
            self.rightchild = self.rightchild.delete(data, root)
        else:
            if self.leftchild is None:
                if self == root:
                    temp = self.minValnode(self.rightchild)
                    self.data = temp.data
                    self.rightchild = self.rightchild.delete(temp.data, root)
                temp = self.rightchild
                self = None
                return temp
            elif self.rightchild is None:
                if self == None:
                    temp = self.maxValnode(self.rightchild)
                    self.data = temp.data
                    self.leftchild = self.leftchild.delete(temp.data, root)
                temp = self.leftchild
                self = None
                return temp
            temp = self.minValnode(self.rightchild)
            self.data = temp.data
            self.rightchild = self.rightchild.delete(temp.data, root)
        return self

    def find(self, data):
        if (data == self.data):
            return True
        elif data < self.data:
            if self.leftchild:
                return self.leftchild.find(data)
            else:
                return False
        else:
            if self.rightchild:
                return self.rightchild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.data), end=' ')
            if self.leftchild:
                self.leftchild.preorder()
            if self.rightchild:
                self.rightchild.preorder()

    def inorder(self):
        if self:
            if self.leftchild:
                self.leftchild.inorder()
            print(str(self.data), end=' ')
            if self.rightchild:
                self.rightchild.inorder()

    def postorder(self):
        if self:
            if self.leftchild:
                self.leftchild.postorder()
            if self.rightchild:
                self.rightchild.postorder()
            print(str(self.data), end=' ')


class tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data, self.root)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        if self.root is not None:
            print()
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()


if __name__ == '__main__':
    tree = tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    print(tree.find(1))
    print(tree.find(12))
    ''' Following tree is getting created:
                    10
                 /      \
               5         12
              / \           \
            4     8          20
                 /          /
                7         15
                         /
                       13
    '''

    tree.preorder()
    tree.inorder()
    tree.postorder()
    print('\n\nAfter deleting 20')
    tree.delete(20)
    tree.inorder()
    tree.preorder()
    print('\n\nAfter deleting 10')
    tree.delete(10)
    tree.inorder()
    tree.preorder()
