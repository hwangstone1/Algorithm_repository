import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
visit = [0 for _ in range(n+1)]
graph = [[0]*(n+1) for _ in range(n+1)]

def dfs(v):
    cnt = 0
    for i in range(1,n+1):
        if visit[i] == 0 and graph[v][i] == 1:
            visit[i] = 1
            dfs(i)

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs(1)
print(visit.count(1) - 1)
