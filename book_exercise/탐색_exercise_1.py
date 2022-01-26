# bfs 음료수 얼려먹기//

from collections import deque
n, m = map(int, input().split())

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    if array[x][y] == 1:
        return False
    while queue:
        x, y = queue.popleft()
        array[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0:
                queue.append((nx, ny))
    return True


array = [list(map(int, input().split())) for _ in range(n)]



result =0

for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            result += 1

print(result)

###### DFS 풀이

# n, m = map(int, input().split())
# array = []
# for i in range(n):
#     array.append(list(map(int, input())))
#
# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#
#     if array[x][y] == 0:
#         array[x][y] = 1
#         dfs(x-1, y)
#         dfs(x+1, y)
#         dfs(x, y-1)
#         dfs(x, y+1)
#
#         return True
#     return False
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1
# print(result)