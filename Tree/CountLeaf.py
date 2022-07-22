from BinarySearchTree import node

def countLeaf(root):
    if root is None:
        return 0
    if(root.leftchild is None and root.rightchild is None):
        return 1
    else:
        return countLeaf(root.leftchild) + countLeaf(root.rightchild)

if __name__=='__main__':
    root = node(3)
    root.insert(2)
    root.insert(1)
    root.insert(4)
    # root.insert(5)
    root.inorder()
    print('\n',countLeaf(root))