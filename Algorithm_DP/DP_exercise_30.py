# baekjoon DP 동전 1

# n = 1 , 1
# n = 2 ,
n, k = map(int, input().split())
print(n, k)
c = [int(input()) for i in range(n)]
dp = [0 for i in range(k+1)]
dp[0] = 1

for i in c:
    for j in range(i, k+1):
        if j-1 >= 0
            dp[j] += dp[j-i]

print(dp[k])