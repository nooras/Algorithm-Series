class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ReverseSubPartLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while True:
                if current.next is None:
                    break
                current = current.next
            current.next = newNode

    def reverse(self):
        current = self.head
        prev = None
        while current:
            nextTemp = current.next
            current.next = prev
            prev = current
            current = nextTemp
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next



    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

def addd(self, rll, temp):
    prev = None
    current = rll
    # print(current, temp)
    while True:
        if current is None or current.next is None:
            break
        prev = current
        current = current.next
    curr = temp
    # print(prev)
    while curr:
        #print(curr.data)
        if rll is None:
            current = curr
            print(current, "Current")
        else:
            current.next = curr
        curr = curr.next
    while current:
        print(current.data)
        current = current.next



rll = ReverseSubPartLL()
x = [2,4,3,8,6,5,1,12]
temp = ReverseSubPartLL()
for y in range(len(x)):
    if x[y] % 2 == 0:
        temp.insert(x[y])
        # print(y)
    else:
        if temp.isListEmpty() is False:
            # print("hii")
            temp.reverse()
            rll = addd(rll.head, temp.head)
            temp = ReverseSubPartLL()
        if x[y]%2 != 0:
            rll.insert(x[y])
# rll.insert(1)
# rll.insert(2)
# temp = rll.insert(3)
rll.print_list()
# # rll.reverse()
# print("------------")
# rll.print_list()

