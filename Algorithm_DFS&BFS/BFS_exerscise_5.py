from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
m, n, h = map(int, input().split())
array = [[list(map(int, input().split())) for i in range(n)] for _ in range(h)]
q = deque([])
result = 0

def bfs(result,q):
    cnt = result
    while q:
        cnt, x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if array[nx][ny][nz] == 0 and array[nx][ny][nz] != -1:
                    array[nx][ny][nz] = 1
                    q.append([cnt+1, nx, ny, nz])
    return cnt

def check(array,result):
    for i in range(h):
        for j in range(n):
            for z in range(m):
                if array[i][j][z] == 0:
                    return -1
    return result


for i in range(h):
    for j in range(n):
        for z in range(m):
            if array[i][j][z] == 1:
                q.append([result, i, j, z])

result = bfs(result,q)
print(check(array,result))