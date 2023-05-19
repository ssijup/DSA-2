def insertion(array):
    arrayLength = len(array)
    for i in range(1,arrayLength) :
        rightFirstElement = array[i]
        j = i-1
        while j >=0 and array[j] > rightFirstElement :
            array[j + 1] = array[j]
            j -=1
        array[j + 1] = rightFirstElement
    return array

arr= [5,6,7,9,0,0,0,0,00,2,4,6]
print(insertion(arr))