class Stack:
    def __init__(self,capacity):
        self.capacity =  capacity
        self.sarray=[None] * capacity
        self.top = -1

    def isFull(self):
        if self.top == self.capacity -1 :
            print("The stack is Full")

    def isEmpty(self):
        if self.top == -1 :
            print("The stack is empty")

    def push(self,item):
        if self.isFull():
            print("Sorry the stack is full")
        else :
            self.top +=1
            self.sarray[self.top] = item
            print(f"The number {item} inserted sucessfully")
        
    def pop(self):
        if self.isEmpty():
            print("Sorry the stack is empty ,unable it pop")
        else:
            print()
            self.sarray[self.top] = None
            self.top -= 1

    def peek(self):
        value = self.sarray[self.top]
        print(f"The value at the top is {value}")

    def display(self):
        for i in range((self.capacity)):
            value = self.sarray[i]
            print(value)
            # self.top -=1

s=Stack(3)
s.push(1)
s.push(2)
s.push(3)
s.display()
s.pop()
s.display()
s.peek()
