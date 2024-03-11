
def InsertionSort(array):

    for i in range(1 , len(array)):
        chave = array[i]
        comparator = i -1
        
        while comparator >= 0 and array[comparator] > chave:
            array[comparator + 1] = array[comparator]
            comparator -= 1
        
        array[comparator + 1] = chave
        
    print(array) 
        
        
    
arr = list(map(int, input().split()))
InsertionSort(arr)

