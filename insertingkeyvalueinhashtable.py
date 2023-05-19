class Hash:
    def __init__(self , capacity)  :
        self.arrayTable = [None] * capacity


    def hashfun(self,key,l) :
        l=l
        val = 0
        for i in key :
            val = (val + ord(i)) % l
        return val

    def setKeyValue(self,key,value) :
        index = self.hashfun(key,10)
        if self.arrayTable[index] is None :
            self.arrayTable[index] = [[key , value]] 
            print("Inserted successfully")

h=Hash(10)
# array = { ,"ram" : "11"}
h.setKeyValue("siju" , 7)
