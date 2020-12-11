'''
CircularLinkedList :

append
prepend
remove
__len__
splitList
print_list
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head

    def prepend(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.head.next = self.head
        else:
            current = self.head
            newNode.next = current
            while current:
                current = current.next
                if current.next == self.head:
                    break
            current.next = newNode
            self.head = newNode

    def remove(self, data):
        current = self.head
        if current.data == data:
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == data:
                    prev.next = current.next
                    current = current.next

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def splitList(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = size//2
        count = 0
        prev = None
        current = self.head
        while current and count< mid:
            count +=1
            prev = current
            current = current.next
        prev.next = self.head

        secondList = CircularLinkedList()
        while current.next != self.head:
            secondList.append(current.data)
            current = current.next
        secondList.append(current.data)

        self.print_list()
        print("\n")
        secondList.print_list()

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            if current == self.head:
                break

cll = CircularLinkedList()
cll.append(2)
cll.append(4)
cll.append(6)
cll.prepend(8)
cll.prepend(8)
# cll.remove(6)
cll.print_list()
print("-----------")
# print(len(cll))
cll.splitList()