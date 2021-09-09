# 보물섬 bfs
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

def bfs(x,y):
    q = deque()
    q.append((x, y))
    max_result = 0
    while q:
        a, b = q.popleft()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if 0 <= na < n and 0 <= nb < m and visit[na][nb] == 0 and array[na][nb] != 'W':
                visit[na][nb] = 1
                array[na][nb] = array[a][b] + 1
                max_result = max(max_result, array[na][nb])
                q.append((na, nb))
    return max_result
n, m = map(int, input().split())
array = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if array[i][j] != 'W':
            visit = [[0]*m for _ in range(n)]
            array[i][j] = 0
            visit[i][j] = 1
            result = max(result, bfs(i, j))

print(result)