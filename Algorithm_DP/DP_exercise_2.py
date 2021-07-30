n = int(input())
number = 1000001
array = [0]*number
array[1] , array[2] = 1 , 2
for i in range(3,n+1):
    array[i] = (array[i-1] + array[i-2])%15746
print(array[n])