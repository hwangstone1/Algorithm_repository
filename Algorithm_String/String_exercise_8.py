# 세로읽기

array = [[False]*15 for _ in range(5)]

for i in range(5):
    data = input() # 한줄씩 받음
    data_len = len(data)
    for j in range(data_len):
        array[i][j] = data[j]

for i in range(15):
    for j in range(5):
        if array[j][i] == False:
            continue
        print(array[j][i], end='')