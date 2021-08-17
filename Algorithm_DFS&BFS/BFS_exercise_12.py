from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
array = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    array[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for i in array[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)
check = -99
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = 0
if check == -99:
    print(-1)