class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def Push(self,data):
        current = self.head
        Newnode = Node(data)
        if self.head == None:
            self.head = Newnode
        else:
            Newnode.next = self.head
            self.head = Newnode

    def Pop(self):
        current = self.head
        if self.head is None :
            print("The stach is Empty")
        else :
            head = self.head
            self.head = self.head.next
            head.next = None

    def peek(self):
        value = self.head.data
        print(f"The top element is : {value}")
    
    def display(self):
        current = self.head
        while current is not None :
            print(current.data)
            current = current.next

s=Stack()
s.Push(11)
s.Push(12)
s.Push(13)
s.display()