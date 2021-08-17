# 경쟁적 전염

from collections import deque
import sys
sys.setrecursionlimit(10000)
n, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
S, X, Y = map(int, input().split())
check = [[0]*n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

q = deque()

def bfs():

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if check[nx][ny] == 0 and array[nx][ny] == 0:
                    array[nx][ny] = array[x][y]
                    check[nx][ny] = check[x][y] + 1
                    q.append((nx,ny))
    return check
def visit(cnt):
    if cnt == k+1:
        bfs()
        return
    for i in range(n):
        for j in range(n):
            if array[i][j] == cnt:
                q.append((i, j))
    visit(cnt+1)

visit(1)

if S < check[X-1][Y-1] :
    print(0)
else:
    print(array[X-1][Y-1])