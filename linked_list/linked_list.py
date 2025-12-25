
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):

        node = Node(data, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def insert_after(self, target, data):
        temp = self.head
        while temp and temp.data != target:
            temp = temp.next

        if temp is None:
            print("Target node not found")
            return

        node = Node(data, temp.next)
        temp.next = node

        if temp == self.tail:
            self.tail = node

    def delete(self, data):
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data == data:
                prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                return
            prev = curr
            curr = curr.next

        print("Value not found")

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " -> "
            itr = itr.next
        print(llstr + "None")

    def remove_duplicates(self):
        current_node = self.head
        while current_node is not None:
            nxt_node = current_node.next
            while nxt_node is not None and current_node.data == nxt_node.data:
                nxt_node = nxt_node.next


            current_node.next = nxt_node
            if nxt_node == self.tail and current_node.data == nxt_node.data:
                self.tail = current_node
                self.tail.next = None

            current_node = nxt_node

if __name__ == '__main__':
    LL = LinkedList()
    LL.insert_at_beginning(6)
    LL.insert_at_end(10)
    LL.insert_after(6, 7)
    LL.insert_at_end(5)
    LL.insert_at_end(5)
    LL.display()
    LL.remove_duplicates()
    LL.display()