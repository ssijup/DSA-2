def bubblesort(array):
    arrayLength=len(array)
    for i in range(arrayLength-1) :
        flag=1
        for j in range(arrayLength-1-i) :
            if array[j] > array[j+1] :
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                flag=0
        if flag == 1 :
            break
    return array

array1 =[4,5,7,4,7,9,0,4,3,5,3,33]
arra2 =[7,5,4,4,9]
print(bubblesort(array1),bubblesort(arra2))