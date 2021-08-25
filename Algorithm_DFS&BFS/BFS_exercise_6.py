from collections import deque
import sys
input = sys.stdin.readline
number = 2000001
array = [0]*number

n, k = map(int, input().split())

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            return print(array[x])
        for i in (x-1,x+1,x*2):
            if 0 <= i <= number and array[i] == 0:
                array[i] = array[x] + 1
                q.append(i)
bfs()