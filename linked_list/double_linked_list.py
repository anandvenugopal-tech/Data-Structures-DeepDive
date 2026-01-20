class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_node(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
    def display(self):
        if self.head is None:
            print("You did not enter the number")
        else:
            temp = self.head

        while temp:
            print(temp.data," ", end="--->")
            temp = temp.next
        print("None")

    def display_reverse(self):
        temp = self.tail

        while temp:
            print(temp.data," ", end="--->")
            temp = temp.prev
        print("None")
    def delete(self,data):
        temp = self.head
        prev = None
        if temp is None:
            print("The list is empty")
        else:
            if temp.data == data:
                self.head = temp.next
                if temp.next is None:
                    self.head = None
                return
            while temp.data != data:
                prev = temp
                temp = temp.next
            if temp.data == self.tail:
                prev = self.tail
                self.tail = None
        prev.next = temp.next
    def insert_after(self,next_to,data):
        node = Node(data)
        temp = self.head
        while temp is not None and temp.data != next_to:
            temp = temp.next
        if temp is None:
            return
        if temp == self.tail:
            self.tail.next = node
            self.tail = node
            return

        node.next = temp.next
        temp.next = node

    def insert_before(self,next_before,data):
        node = Node(data)
        temp = self.head
        prev = None
        if temp is None:
            print("Missing number")
        if temp.data == next_before:
            node.next = self.head
            self.head = node
            return
        while temp is not None and temp.data != next_before:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        if temp == self.tail:
            self.tail.prev = node
            return

        prev.next = node
        node.next = temp




Dl = DLinkedList()
Dl.add_node(10)
Dl.add_node(20)
Dl.add_node(30)
Dl.display()
Dl.display_reverse()

Dl.insert_before(10,5)
Dl.display()