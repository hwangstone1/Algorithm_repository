from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
number = 100001
check = [0] * number


def bfs():
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            print(check[x])
            return
        for i in (x-1, x+1, x*2):
            if 0 <= i < number and check[i] == 0:
                if i == x*2 and x != 0:
                    check[i] = check[x]
                    q.appendleft(i)
                else:
                    check[i] = check[x] + 1
                    q.append(i)
bfs()
