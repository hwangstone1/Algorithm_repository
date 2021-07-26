from collections import deque
t = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs(x, y, ex, ey):
    array[x][y] = 1
    queue = deque()
    queue.append((x,y))
    while queue:
        x , y = queue.popleft()
        if x == ex and y == ey:
            return array[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if array[nx][ny] == 0:
                    array[nx][ny] = array[x][y] + 1
                    queue.append((nx,ny))

for i in range(t):
    n = int(input())
    array = [[0]*n for i in range(n)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    if sx == ex and sy == ey :
        print(0)
        continue
    result = bfs(sx, sy, ex, ey)
    print(result)