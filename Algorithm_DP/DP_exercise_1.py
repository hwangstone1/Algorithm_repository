t = int(input())
array = [0]*101
array[1] , array[2] , array[3] = 1, 1, 1

while t:
    n = int(input())
    for i in range(4, n+1):
        array[i] = array[i-2] + array[i-3]
    print(array[n])
    t -= 1
