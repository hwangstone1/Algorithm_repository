# 방번호
# 1 자리면 1 세트
# 2 자리면 서로다르면 2세트 6 or 9 이면 한세트

import sys

input = sys.stdin.readline().strip()

string = input()
cnt =-0
six_nine = 0
for i in range(len(string)):
    if string[i] != '6' or string[i] != '9':
        if string[i] == string[i+1]:
            cnt += 1
    else:
        six_nine += 1
print(cnt + (six_nine)//2)