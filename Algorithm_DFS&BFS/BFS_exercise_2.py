from collections import deque
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i] , y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                queue.append((nx,ny))
bfs(0,0)
print(array[n-1][m-1])