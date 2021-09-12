# 문자열 1120

a , b = list(input().split())
mini = 50

for i in range(len(b)- len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1

    if cnt < mini:
        mini = cnt
print(mini)