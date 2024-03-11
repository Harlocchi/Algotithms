def ReverseArray(array):
    auxArr = []
    
    for i in range(len(array)):
        auxArr.append(array[(len(array) - 1) - i])
    print(auxArr)
arr = list(map(int, input().split()))
ReverseArray(arr)