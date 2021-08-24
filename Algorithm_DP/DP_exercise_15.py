#가장 긴 증가하는 부분 수열
length = int(input())
array = list(map(int, input().split()))
dp = [1]*length

for i in range(1, length):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))