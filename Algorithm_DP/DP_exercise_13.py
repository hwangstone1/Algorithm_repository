#정수 삼각형
floor = int(input())
array = []
for i in range(floor):
    array.append(list(map(int, input().split())))

for i in range(1, floor):
    for j in range(i+1):
        if j == 0:
            left_up = 0
        else:
            left_up = array[i-1][j-1]
        if i == j:
            right_up = 0
        else:
            right_up = array[i-1][j]
        array[i][j] = array[i][j] + max(left_up, right_up)
print(max(array[floor-1]))