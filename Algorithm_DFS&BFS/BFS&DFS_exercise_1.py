# 삼성 기출문제 연구소

from collections import deque
from copy import deepcopy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split()) # n 행 m 열
array = [list(map(int, input().split())) for _ in range(n)]

count = 0
def sw_bfs():
    global count
    q = deque(())
    visit = [[0]*m for _ in range(n)]
    backup = deepcopy(array)
    for i in range(n):
        for j in range(m):
            if backup[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()

        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]

            if 0 <= newx < n and 0 <= newy < m:
                if visit[newx][newy] == 0 and backup[newx][newy] == 0:
                    visit[newx][newy] = 1
                    backup[newx][newy] = 2
                    q.append((newx, newy))
    candi = 0
    for i in range(n):
        for j in range(m):
            if backup[i][j] == 0:
                candi += 1
    if count < candi:
        count = candi


def sw_dfs(cnt, sx, sy):
    if cnt == 3:
        sw_bfs()
        return
    for i in range(sx, n):
        for j in range(sy, m):
            if array[i][j] == 0:
                array[i][j] = 1
                sw_dfs(cnt+1, i, j)
                array[i][j] = 0
        sy = 0

sw_dfs(0, 0, 0)
print(count)