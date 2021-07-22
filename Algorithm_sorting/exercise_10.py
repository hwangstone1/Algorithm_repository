import sys
input = sys.stdin.readline
n = int(input())
array_1 = list(map(int, input().split()))
array_2 = sorted(list(set(array_1)))

dic = {array_2[i] : i for i in range(len(array_2))}
for i in array_1:
    print(dic[i],end=' ')
