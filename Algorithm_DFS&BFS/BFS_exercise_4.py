from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
array = [list(map(int, input().split())) for i in range (n)]
result = 0
q = deque([])

def dfs(q,result):
    cnt = result
    while q:
        v = q.popleft()
        cnt = v[0]
        nx = v[1]
        ny = v[2]
        for i in range(4):
            cx = nx+dx[i]
            cy = ny+dy[i]
            if 0 <= cx < n and 0 <= cy < m:
                if array[cx][cy] == 0 and array[cx][cy] != -1:
                    array[cx][cy] = 1
                    q.append([cnt+1,cx,cy])
    return cnt

def check(result,array):
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                return -1
    return result

for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            q.append([result, i, j])
result = dfs(q,result)
print(check(result,array))