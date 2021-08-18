# N-Queen
import sys
input = sys.stdin.readline
n = int(input())
count = 0
array = [0]*15

def promising(cdx):
    for i in range(cdx):
        if array[cdx] == array[i] or cdx-i == abs(array[cdx] - array[i]):
            return 0
    return 1

def backt(cdx):
    global count
    if cdx == n:
        count += 1
        return
    for i in range(n):
        array[cdx] = i
        if promising(cdx):
            backt(cdx+1)

backt(0)
print(count)
"""
n = int(input())

array = [0]*n

def dfs(array, n, row):
    count = 0
    if row == n:
        return 1
    for i in range(n):
        array[row] = i
        for j in range(row):
            if array[j] == array[row]:
                break
            if row - j == abs(array[j]- array[row]):
                break
        else:
            count += dfs(array, n, row+1)
    return count

result = dfs(array, n, 0)
print(result)
"""