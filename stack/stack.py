class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    def push(self,data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return
        self.top = self.top.next


    def display(self):
        current = self.top

        while current is not None:
            print(current.data)
            current = current.next


st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.display()
print("_____________")
st.pop()
st.display()