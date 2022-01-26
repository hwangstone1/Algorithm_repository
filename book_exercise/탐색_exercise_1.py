# bfs 음료수 얼려먹기
from collections import deque
n, m = map(int, input().split())

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    if array[x][y] == 1:
        return False
    while queue:
        x, y = queue.popleft()
        array[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0:
                queue.append((nx, ny))
    return True


array = [list(map(int, input().split())) for _ in range(n)]



result =0

for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            result += 1

print(result)