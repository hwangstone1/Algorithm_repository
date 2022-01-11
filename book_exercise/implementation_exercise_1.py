# 상하좌우
# N = int(input())
# list = list(input().split())
# x, y = 0, 0
# for i in range(0, len(list)):
#     if list[i] == 'R' and y+1 <= N-1 :
#         y += 1
#     elif list[i] == 'L' and y-1 >= 0 :
#         y -= 1
#     elif list[i] == 'U' and x-1 >= 0 :
#         x -= 1
#     elif list[i] == 'D' and x+1 <= N-1:
#         x += 1
#     print(x, y)
#
# print(x+1, y+1)
# ------- 내가 짠 코드 ------
# ------- 정답 코드 ------
n = int(input())
x, y = 1, 1
plans = input().split()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
map = ['L', 'R', 'U', 'D']
for plan in plans:
    for i in range(len(map)):
        if plan == map[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)