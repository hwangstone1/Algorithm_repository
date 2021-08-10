from collections import deque
from copy import deepcopy
import sys
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0] , [0, 0, -1, 1]
count = sys.maxsize

def bfs():
    global count
    candi = 0
    q = deque(())
    visit = [[-1]*n for _ in range(n)]
    map = deepcopy(array)

    for i in range(n):
        for j in range(n):
            if map[i][j] == -1:
                map[i][j] = 0
                visit[i][j] = 0
                q.append((i, j))
            if map[i][j] == 2:
                map[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if map[nx][ny] == 0 and visit[nx][ny] == -1 :
                    visit[nx][ny] = visit[x][y] + 1
                    candi = max(visit[nx][ny], candi)
                    q.append((nx, ny))
    for i in range(n):
        print(visit[i])
    for i in range(n):
        for j in range(n):
            if map[i][j] == 0 and visit[i][j] == -1:
                candi = sys.maxsize
    count = min(count, candi)


def dfs(cnt, start, end):
    if cnt == m :
        bfs()
        return
    for i in range(start, n):
        for j in range(end, n):
            if array[i][j] == 2:
                array[i][j] = -1
                dfs(cnt + 1, i, j)
                array[i][j] = 2

        end = 0

dfs(0, 0, 0)
if count == sys.maxsize:
    print(-1)
else:
    print(count)