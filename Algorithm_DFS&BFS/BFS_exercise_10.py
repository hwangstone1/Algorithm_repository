# 숨바꼭질 4
from collections import deque
n, k = map(int, input().split())
number = 100001
check = [0]* number
walk = [0]* number

def path(x):
    arr = []
    temp = x
    for _ in range(check[x]+1):
        arr.append(temp)
        temp = walk[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            print(check[x])
            path(x)
            return
        for i in (x+1, x-1, x*2):
            newx = i
            if 0 <= newx < number and check[newx] == 0:
                check[newx] = check[x] + 1
                q.append(newx)
                walk[i] = x

bfs()

