from collections import deque
import sys
input = sys.stdin.readline
n, m, v = map(int, input().split())
g = [[0]*(n+1) for i in range(n+1)]
visit = [0]*(n+1)


def bfs(v):
    visit[v] = 1
    queue = deque([v])
    while queue:
        v = queue.popleft()
        print(v,end = ' ')
        for i in range(1,n+1):
            if visit[i] == 0 and g[v][i] == 1:
                queue.append(i)
                visit[i] = 1

for _ in range(m):
    x, y = map(int, input().split())
    g[x][y] = 1
    g[y][x] = 1

bfs(v)