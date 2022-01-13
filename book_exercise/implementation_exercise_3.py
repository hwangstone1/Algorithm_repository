input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
#왼쪽위 , 왼쪽아래 , 위 왼쪽, 위 오른쪽, 오른쪽 위, 오른쪽 아래 , 아래 왼쪽, 아래 오른쪽
moves = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)]
cnt = 0
for move in moves:
    ny = row + move[0]
    nx = column + move[1]

    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        cnt += 1
print(cnt)

