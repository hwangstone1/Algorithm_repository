# 적록색약 = 적색과 녹색을 구분하기 어려운 상태
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
array = [list(input()) for _ in range(n)]
check = [[0]*(n) for _ in range(n)]
check2 = [[0]*(n) for _ in range(n)]
carray = [[0]*n for _ in range(n)]
dx, dy = [-1, 1, 0, 0] , [0, 0, -1, 1]
result = [0,0,0]
def dfs(x, y, array, check):
    check[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if array[nx][ny] == array[x][y] and check[nx][ny] == 0:
                dfs(nx, ny, array, check)
cnt = 0
cnt2 =0
for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            dfs(i, j, array, check)
            cnt += 1

for i in range(n):
    for j in range(n):
        if array[i][j] == 'R' or array[i][j] == 'G':
            carray[i][j] = 1
        else:
            carray[i][j] = 2

for i in range(n):
    for j in range(n):
        if check2[i][j] == 0:
            dfs(i, j, carray, check2)
            cnt2 += 1

print(cnt, cnt2)