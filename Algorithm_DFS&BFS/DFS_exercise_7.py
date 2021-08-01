import sys
sys.setrecursionlimit(10000)

n , m , k = map(int, input().split()) # n = 행 M = 열
array = [[0]*m for _ in range(n)]
check = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(k):
    x , y , x1, y1 = map(int, input().split()) # x 열 y 행
    for i in range(y, y1):
        for j in range(x, x1):
            array[i][j] = 1

cnt = 0
result = []
def dfs(x,y, check):
    global tmp
    array[x][y] = 1
    check[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if array[nx][ny] == 0 and check[nx][ny] == 0:
                tmp += 1
                dfs(nx, ny, check)


for i in range(n):
    for j in range(m):
        if array[i][j] == 0 and check[i][j] == 0:
            tmp = 0
            dfs(i, j, check)
            result.append(tmp+1)
            cnt += 1
print(cnt)
answer = sorted(result)
for i in answer:
    print(i,end=' ')