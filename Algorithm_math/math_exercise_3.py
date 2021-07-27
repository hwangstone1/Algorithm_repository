inta = int(input())
str_list = []
for i in range(1, inta+1):
    str_list.append(str(i))

cnt = 0

print(str_list)

for i in str_list:
	# 문법오류 조심하자
    # '3' or '6' or '9' in i ==>> 안됌!!
    if '3' in i or '6' in i or '9' in i:
        cnt = 0
        for j in i:
            if j == '3' or j == '6' or j == '9':
                cnt += 1
        print('X'*cnt, end=' ')

    else:
        print(i, end=' ')