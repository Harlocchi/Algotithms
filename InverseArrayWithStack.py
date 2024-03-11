def reverse_array(array):
    stack = []
    
    for val in array:
        stack.append(val)
    
    for i in range(len(stack)):
        array[i] = stack.pop()
    
    print(array)
    
arr = list(map(int, input().split()))
reverse_array(arr)