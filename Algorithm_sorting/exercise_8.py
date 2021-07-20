#N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#시간제한 3초 메모리제한 8MB
import sys
input = sys.stdin.readline
n = int(input())
M = 10001
cnt_list = [0]*M
for i in range(n):
    cnt = int(input())
    cnt_list[cnt] += 1

for i in range(M):
    if cnt_list[i] != 0:
        for j in range(cnt_list[i]):
            print(i)
