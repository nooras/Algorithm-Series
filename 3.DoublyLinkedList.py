'''
Doubly Linked List:

append
prepend
add_after_node
add_before_node
delete - 4 Cases
print_list
reverse
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            newNode.prev = None
            newNode.next = None
            self.head = newNode
        else:
            current =self.head
            # print(current.data, "curr")
            while True:
                if current.next is None:
                    break
                # print(current.data, "innn")
                # print("bjbb")
                current = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = None
            # print(newNode.data)

    def prepend(self, data):
        newNode = Node(data)
        if self.head is None:
            newNode.next = None
            newNode.prev = None
            self.head = newNode
        else:
            current = self.head
            newNode.next = current
            newNode.prev = None
            current.prev = newNode
            self.head = newNode

    def add_after_node(self, key, data):
        current =  self.head
        while current:
            if current.next is None and current.data == key:
                self.append(data)
                return
            elif current.data == key:
                newNode = Node(data)
                next = current.next
                current.next = newNode
                newNode.next = next
                newNode.prev = current
                next.prev = newNode
            current = current.next

    def add_before_node(self, key, data):
        current =  self.head
        while current:
            if current.prev is None and current.data == key:
                self.prepend(data)
                return
            elif current.data == key:
                newNode = Node(data)
                prev = current.prev
                current.prev = newNode
                newNode.prev = prev
                newNode.next = current
                prev.next = newNode
            current = current.next

    def delete(self, key):
        current = self.head
        while current:
            if current.data == key and current == self.head:
                # Case 1 - Only 1 Element
                if not current.next:
                    current = None
                    self.head = None
                    return
                # Case 2 - 1 element have to remove
                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return
            # Case 3 - Deleting middle elemnet
            elif current.data == key:
                if current.next:
                    next = current.next
                    prev = current.prev
                    prev.next = next
                    next.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return
                #Case 4 - Deleting last elemnt
                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next
        return print("Element Not Found!!")

    def deleteNode(self, node):
        current = self.head
        while current:
            if current == node and current == self.head:
                # Case 1 - Only 1 Element
                if not current.next:
                    current = None
                    self.head = None
                    return
                # Case 2 - 1 element have to remove
                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return
            # Case 3 - Deleting middle elemnet
            elif current == node:
                if current.next:
                    next = current.next
                    prev = current.prev
                    prev.next = next
                    next.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return
                #Case 4 - Deleting last elemnt
                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next
        return print("Element Not Found!!")

    def reverse(self):
        current = self.head
        while current:
            tmp = current.prev
            current.prev = current.next
            current.next = tmp
            current = current.prev
        if tmp:
            self.head = tmp.prev

    def remove_duplicates(self):
        current = self.head
        seen = dict()
        while current:
            if current.data not in seen:
                seen[current.data] = 1
                current = current.next
            else:
                next = current.next
                self.deleteNode(current)
                current = next

    def pairs_with_sum(self, sum_val):
        pairs = []
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append([p.data, q.data])
                q = q.next
            p = p.next
        return pairs

    def print_list(self):
        current = self.head
        #print(current)
        while current:
            print(current.data)
            current = current.next

li = DoublyLinkedList()
li.append(1)
li.append(2)
li.append(3)
li.prepend(4)
li.prepend(5)
li.append(2)
li.append(3)
li.add_after_node(1,50)
li.add_before_node(1,100)
# li.delete(4)
# print("-----------")
li.print_list()
print("-----------")
li.reverse()
li.print_list()
print("-----------")
li.remove_duplicates()
li.print_list()
print("-----------")
print(li.pairs_with_sum(6))
