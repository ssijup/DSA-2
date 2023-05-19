class LinearProbing :
    def __init__(self,capacity) :
        self.table = [None] * capacity

    def hashh(self , key) :
        value = 0
        for i in key :
            value = value + ord(i)
        return value % len(self.table)
    
    def linearprobing(self ,key ,value) :
        index = self.hashh(key)
        if self.table[index] is None :
            self.table[index] = [[key ,value]]
            print("First time")
            return
        else :
            while self.table[index] is not None and self.table[index][0][0] !=0 :
                print("uu")
                index = (index + 1) % len(self.table)
            if self.table[index] is None :
                self.table[index] = [[key ,value]]
                print("Done none")
            elif self.table[index][1][0] == key :
                self.table[index][0][1] = value
                print("Done value updation")


l=LinearProbing(5)
l.linearprobing("siju" , 1)
print("back1")
l.linearprobing("siju" ,7)
print("back 2")

