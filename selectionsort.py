def selection(array) :
    size = len (array)
    for i in range(size-1) :
        for j in range(i + 1,size) :
            if array[i] > array[j] :
                array[j],array[i] = array[i],array[j]
    return array


arr= [45,34,7,12,467,00,12,00,]
print(selection(arr))  