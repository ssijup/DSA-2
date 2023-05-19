class Queue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.qarray = [None] * capacity
        self.rear=-1
        self.front=0
        self.size=0

    def isFull(self):
        if self.size == self.capacity:
            print("The QUEUE is full ")
    
    def isEmpty(self):
        if self.size == 0 :
            print("The QUEUE is empty")
    
    def enqueue(self,item) :
        if self.isFull() :
            print("The queue is full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.qarray[self.rear] = item
        self.size += 1
        print(f"The  {item} has been inserted sucessfully")

    def dequeue(self):
        if self.isEmpty() :
            print("The queue is Empty ")
            return
        self.qarray[self.front]=None
        self.front= (self.front + 1) % self.capacity
        self.size -= 1
    
    def display(self) :
        current = self.front
        print ("The Queue list are :")
        for i in range(self.rear) :
            print(self.qarray[current])
            current = current + 1
    
    def peek(self):
        current=self.front
        item = self.qarray[current]
        print(item,"The the first emement ")
    
    def rearr(self):
        current=self.rear
        item = self.qarray[current]
        print(item,"The the last emement ")

q=Queue(5)
q.isEmpty()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.peek()
q.rearr()
q.display()
q.dequeue()
q.rearr()
q.peek()
q.display()







