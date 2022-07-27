import SinglyLinkedList

def checkLenght(lists):
    count = 0
    temp = lists.head
    while(temp!=None):
        count+=1
        temp = temp.next
    return count

if __name__ == '__main__':
    mylists = SinglyLinkedList.Linkedlist()
    for i in range(1,11):
        mylists.insertBgning(i)
    mylists.printList()
    print()
    print('Lenght: ',checkLenght(mylists))