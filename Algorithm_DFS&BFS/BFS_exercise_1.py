n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input())))
cnt = 0
result = 0
numbers = []
def dfs(x,y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return 0
    if array[x][y] == 1:
        cnt += 1
        array[x][y] = 0

        #상
        dfs(x-1,y)
        #하
        dfs(x,y-1)
        #좌
        dfs(x+1,y)
        #우
        dfs(x,y+1)
        return 1
    return 0

for i in range(n):
    for j in range(n):
        if dfs(i,j) == 1:
            result += 1
            numbers.append(cnt)
        cnt = 0
numbers = sorted(numbers)
print(result)
for i in numbers:
    print(i)