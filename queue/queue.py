class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,data):
        node = Node(data)
        if self.rear is None:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front is None:
            print("Empty")
        self.front = self.front.next
        if self.front is None:
            self.rear = None

    def display(self):
        current = self.front
        if self.front is None:
            print("The list is empty")
        while current is not None:
            print(current.data)
            current = current.next

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("__________")
q.dequeue()
q.display()

