# 왕실의 나이트 이코테 exercise(구현)

now = input()
row = int(now[1]) # 행
colum = int(ord(now[0]) - int(ord('a'))+1) # 열
steps = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (2, -1), (2, 1), (1, -2), (1, 2)]

result = 0
for i in steps:
    next_row = row + i[0]
    next_colum = colum + i[1]
    if 0 < next_row < 9 and 0 < next_colum < 9:
        result += 1
print(result)