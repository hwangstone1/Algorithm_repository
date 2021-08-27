# 못생긴수
n = int(input())
array =[0]*n
array[0] = 1
i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5
for i in range(1, n):
    array[i] = min(next2, next3, next5)
    if array[i] == next2:
        i2 += 1
        next2 = array[i2]* 2
    if array[i] == next3:
        i3 += 1
        next3 = array[i3] * 3
    if array[i] == next5:
        i5 += 1
        next5 = array[i5] * 5
print(array[n-1])
