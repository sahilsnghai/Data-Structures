class Tree(object):
    def __init__(self,data=None):
        self.root=data
        self.right = None
        self.left=None
    
    def setleft(self,data):
        self.left = data
    
    def setright(self,data):
        self.right = data
    
    def getleft(self):
        return self.left
    
    def getright(self):
        return self.right
    
    def setdata(self,data):
        self.root = data
    
    def getdata(self):
        return self.root
    
def inorder(Tree):
    if Tree:
        inorder(Tree.getleft())
        print(Tree.getdata(), end=' ')
        inorder(Tree.getright())
    return 


def preorder(Tree):
    if Tree:
        print(Tree.getdata(), end=' ')
        preorder(Tree.getleft())
        preorder(Tree.getright())
    return

def postorder(Tree):
    if Tree:
        postorder(Tree.getleft())
        postorder(Tree.getright())
        print(Tree.getdata(), end=' ')
    return
if __name__=='__main__':
    root = Tree(1)
    root.setleft(Tree(2))
    root.setright(Tree(3))
    root.left.setleft(Tree(4))
    root.right.setright(Tree(5))

    print('Inorder Traversal')
    inorder(root)
    # print('\nPreorder Traversal')
    # preorder(root)
    # print('\nPostorder Traversal')
    # postorder(root)

    root.left.left.setleft(Tree(6))
    print('Inorder Traversal')
    inorder(root)
