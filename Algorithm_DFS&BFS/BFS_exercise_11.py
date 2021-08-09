from collections import deque
n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0] , [0, 0, -1, 1]

def bfs():
    q = deque(())
    q.append((0, 0, 1))
    visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visit[0][0][1] = 1
    while q:
        x, y, c = q.popleft()
        if x == n - 1 and y == m - 1:
            return visit[x][y][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if array[nx][ny] == 1 and c == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    q.append((nx, ny, 0))
                elif array[nx][ny] == 0 and visit[nx][ny][c] == 0:
                    visit[nx][ny][c] = visit[x][y][c] + 1
                    q.append((nx, ny, c))
    return -1

print(bfs())