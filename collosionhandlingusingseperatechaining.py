class Node:
    def __init__(self,key,value) :
        self.key = key
        self.value = value
        self.next = None

class Seperatechaining :
    def __init__(self,capacity) :
        self.capacity =capacity
        self.size = 0
        self.table = [None] * capacity

    def hashh(self,key) :
        capacity = 10
        value = 0
        for i in key :
            value = (value + ord(i)+ 23) % capacity
        return value
    
    def insert(self,key,value) :
        index = self.hashh(key)
        newnode = Node(key ,value)
        if self.table[index] is None :
            self.table[index] = newnode
            print(f"Inserted {newnode.value}")
        else:
            current =self.table[index]
            while current :
                if current.key == key :
                    current.value = value
                    return
                current = current.next

            newnode.next = self.table[index]
            self.table[index] = newnode
            print(f"Inserted okeyy {value}")
            self.size +=1 
            

    def remove(self,key) :
        index = self.hashh(key)
        current = self.table[index]
        previous = None
        if self.table[index] is not None :
            while current :
                if current.key == key :
                    if previous :
                        previous.next = current.next
                    else :
                        self.table[index] = current .next
                    return
                previous = current
                current = current.next

    def search(self,key) :
        index = self.hashh(key)
        current = self.table[index]
        while current :
            if current.key == key :
                print("value", current.value)
            current = current.next
    
    def display(self) :
        for key ,value in enumerate(self.table) :
            if value is not None :
                print(f"Key- {key} : Index- {value}")

             
sc=Seperatechaining(10)
sc.insert("rambo" , 23)
sc.insert("raju" ,2)
print("gau")
sc.insert("gautham" ,3)
print("dis")
sc.display()
sc.search("raju")
sc.remove("raju")
sc.display()