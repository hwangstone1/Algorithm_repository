# 계수정렬

array = list(map(int ,input().split()))

count = [0] * (len(array)+1)
for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

