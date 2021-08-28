# 오르막 수
n = int(input())
dp = [[0 for i in range(10)] for j in range(1001)]
for i in range(10):
        dp[0][i] = 1
for i in range(1, n+1):
    for j in range(10):
        if j == 0 :
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
result = 0
for i in range(n):
    result += sum(dp[i])
print(result % 10007)