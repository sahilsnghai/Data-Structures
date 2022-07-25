class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def printPath(node, path=[]):
    if node is None:
        return
    path.append(node.data)

    if (node.left is None) and (node.right is None):
        print(' '.join(str(i) for i in path if i != 0))
    else:
        printPath(node.left, path)
        printPath(node.right, path[:1])


if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.right.left = node(5)

    printPath(root)
