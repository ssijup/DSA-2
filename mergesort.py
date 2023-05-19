def partition(array):
    if len(array) > 1 :
        midindex = len(array) // 2
        rightArray = array[ : midindex]
        leftArray = array[midindex : ]
        partition(rightArray)
        partition(leftArray)

        i = j = k = 0
        while i < len(rightArray) and j < len(leftArray) :
            if rightArray[i] < leftArray[j] :
                array[k] = rightArray[i]
                i+=1
            else:
                array[k] = leftArray[j]
                j+=1
            k+=1

        while i < len(rightArray) :
            array[k] = rightArray[i]
            i +=1
            k +=1
        while j < len(leftArray):
            array[k] = leftArray[j]
            j +=1
            k +=1
        return array

arr =[99,88,66,77,44,66,33,55,77,6,4,3]
print(arr)
s=partition(arr)
print(s)