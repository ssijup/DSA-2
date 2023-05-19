class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.rear=None
        self.front=None
  
    def isEmpty(self):
        if self.rear == None:
            print("The Queue is empty")
    
    def enqueue(self,data):
        current = self.rear
        Newnode = Node(data)
        if self.rear is None :
            self.rear = self.front = Newnode
        else:
            self.rear.next=Newnode
            self.rear=Newnode
        
    def dequeue(self):
        if self.isEmpty():
            print("The Queue is Empty")
            return
        if self.rear == self.front :
            self.rear = self.front = None 
        else :
            self.front = self.front.next
        
    def peek(self):
        data= self.front.data
        print(data,"The first element")


    def display(self):
        current = self.front
        while current is not None :
            print(current.data)
            current = current.next
    
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.enqueue(4)
q.dequeue()
q.display()
q.peek()
q.display()

