#에라토스테네스의체

n, k = map(int, input().split())
ch = [0]*(n+1)
count = 0
result = 0

for i in range(2, n+1):
    if ch[i] == 0:
        for j in range(i, n+1, i):
            if ch[j] == 0:
                count += 1
                result = j
                if count == k:
                    print(result)
                    break
            ch[j] = 1