import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, h):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if array[nx][ny] > h and check[nx][ny]:
                check[nx][ny] = 1
                dfs(nx, ny, h)

result = 1
for h in range(max(map(max, array))):
    check = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and array[i][j] > h:
                cnt += 1
                check [i][j]= 1
                dfs(i, j, h)

    result = max(cnt,result)
print(result)
