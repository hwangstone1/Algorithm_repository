n, m = map(int, input().split())
array = [[0]*(n+1) for _ in range(n+1)]
visit = [-1]*(n+1)
cnt = 0
for i in range(m):
    x, y = map(int, input().split())
    array[x][y] = 1
    array[y][x] = 1

def dfs(v):
    visit[v] = 1
    for i in range(1,n+1):
        if visit[i] == -1 and array[v][i] == 1:
            dfs(i)


for i in range(1,n+1):
    if visit[i] == -1 :
        dfs(i)
        cnt += 1

print(cnt)