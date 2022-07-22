class Node(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, val):
        self.root = Node(val)

    def insertNode(root, val):
        if root == None:
            root = Node(val)
        elif (root.data < val):
            root.right = Tree.insertNode(root.right, val)
        else:
            root.left = Tree.insertNode(root.left, val)

        return root

    def inorder(root):
        if root==None:
            return
        else:
            Tree.inorder(root.left)
            print(root.data,end=' ')
            Tree.inorder(root.right)
   
    def preorder(root):
        if root==None:
            return
        else:
            print(root.data,end=' ')
            Tree.preorder(root.left)
            Tree.preorder(root.right)
    
    def postorder(root):
        if root==None:
            return
        else:
            Tree.postorder(root.left)
            Tree.postorder(root.right)
            print(root.data,end=' ')


if __name__ == '__main__':
    array = [22, 2, 41, 45, 23, 12, 43, 54, 65, 78, 87]
    treenode = Node(array[6])
    print(treenode.data)
    for i in range(1, len(array)-1):
        treeroot = Tree.insertNode(treenode, array[i])
    print('\nInorder: ' )
    Tree.inorder(treeroot)
    print('\nPreorder: ')
    Tree.preorder(treeroot)
    print('\nPostorder: ')
    Tree.postorder(treeroot)
