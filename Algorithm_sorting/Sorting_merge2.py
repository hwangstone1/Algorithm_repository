import sys
input = sys.stdin.readline
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

def mergesort(arr):
    n = len(arr)
    if n > 1:
        mid = (n//2)
        l = arr[:mid]
        r = arr[mid:]
        left = mergesort(l)
        right = mergesort(r)
        return merge(left, right)
    else:
        return arr

def merge(left,right):
    i, j = 0, 0
    tmp = []
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
    while i < len(left):
            tmp.append(left[i])
            i += 1
    while j < len(right):
            tmp.append(right[j])
            j += 1
    return tmp

result = mergesort(array)
print(result)