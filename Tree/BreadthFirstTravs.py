class node:
    def __init__(self, data =None):
        self.data = data
        self.rightchild =None
        self.leftchild =None 

def height(node):
    if node is None:
        return 0
    else:
        leftheight = height(node.leftchild)
        rightheight =height(node.rightchild)

        if leftheight > rightheight:
            return leftheight + 1
        else:
            return rightheight + 1

def breathTravl(root):
    if root == None:
        return 0
    else:
        h =height(root)
        for i in range(1,h+1):
            printBFT(root,i)

def printBFT(root , level):
    if root is None:
        return
    else:
        if level == 1:
            print(root.data, end=' ')
        elif level > 1:
            printBFT(root.leftchild, level -1)
            printBFT(root.rightchild, level -1)

if __name__=="__main__":
    root =node(1)
    root.leftchild =node(2)
    root.rightchild =node(3)
    root.leftchild.leftchild =node(4)
    root.rightchild.rightchild= node(5)

    breathTravl(root)