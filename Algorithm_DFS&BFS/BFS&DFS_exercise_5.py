# 게리맨더링 1






n = int(input())

people = [list(map(int, input().split()))]
arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    new_tmp = tmp[1:]
    for j in new_tmp:
        arr[i][j] = 1

for i in range(n):
    print(arr[i])
