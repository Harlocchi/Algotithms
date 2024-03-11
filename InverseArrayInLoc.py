def reverse_Array(array):
    
    init = 0
    end = len(array) - 1
    
    while end > init:
        array[init], array[end] = array[end], array[init]
        init += 1
        end -= 1
    
    print(array)
    
    
arr = list(map(int, input().split()))
reverse_Array(arr)
    