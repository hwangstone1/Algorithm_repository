n, m = map(int, input().split())
array = list(map(int ,input().split()))
check = [0] * 11

for i in array:
    check[i] += 1

result =0
for i in range(1, m+1):
    n -= check[i]
    result += check[i]*n

print(result)