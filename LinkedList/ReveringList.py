from cmath import sin
import SinglyLinkedList


def reverser(lists):
    previous = None
    current = lists.head
    while (current != None):
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    lists.head = previous


if __name__ == '__main__':
    myLinkedList = SinglyLinkedList.Linkedlist()
    for i in range(10, 0, -1):
        myLinkedList.insertBgning(i)

    print('Original:', end=' ')
    myLinkedList.printList()
    print()
    print('Reversed:', end=' ')
    reverser(myLinkedList)
    myLinkedList.printList()
