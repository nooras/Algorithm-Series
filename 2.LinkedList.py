'''
Singly Linked List:

isListEmpty
insert
insertHead
insertPos
listLength
print_list
deleteEnd
deleteHead
deleteAt
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    # Inserting at the end
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            #self.head.next = newNode a->c not b->c
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    #Inserting at start
    def insertHead(self, newNode):
        temporary = self.head
        self.head = newNode
        self.head.next = temporary
        del temporary

    # Inserting at position or betwen
    def insertPos(self, newNode, position):
        if position == 0:
            self.insertHead(newNode)
            return
        if position < 0 or position > self.listLength():
            print("Invalid Position")
            return
        count = 0
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            if count == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            count +=1

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length +=1
            currentNode = currentNode.next
        return length

    def printList(self):
        if self.head is None:
            print("Empty Linkedlist")
        currentData = self.head
        while True:
            if currentData is None:
                break
            print(currentData.data)
            currentData = currentData.next

    def deleteEnd(self):
        node = self.head
        while node.next is not None:
            previosNode = node
            node = node.next
        previosNode.next = None

    def deleteHead(self):
        if self.isListEmpty() is False:
            previosNode = self.head
            self.head = self.head.next
            previosNode.next = None
        else:
            print("LL is empty")

    def deleteAt(self, position):
        if position < 0 or position >= self.listLength():
            print("Invalid Position")
            return
        if self.isListEmpty() is False:
            if position is 0:
                self.deleteHead()
                return
            count = 0
            node = self.head
            while True:
                if count == position:
                    previousNode.next = node.next
                    node.next = None
                    break
                previousNode = node
                node = node.next
                count += 1

firstNode = Node("Fam")
linkedlist = LinkedList()
linkedlist.insert(firstNode)
firstNode = Node("Nooras")
linkedlist.insert(firstNode)
node = Node("Fatima")
linkedlist.insertHead(node)
node = Node("gm")
# linkedlist.insertPos(node, 20)
linkedlist.printList()
print("--------")
# linkedlist.deleteEnd()
linkedlist.deleteAt(0)
linkedlist.printList()