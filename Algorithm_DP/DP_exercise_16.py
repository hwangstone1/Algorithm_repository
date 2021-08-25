# 2xN 타일링 2
"""
n = 2  ==> 3
n = 3  ==> 5
n = 4  ==> 11
N = 5 ==> 21
N = 6  ==> 43
n = 7 ==> 85
n = 8 ==> 171

... 따라서 f(n) = 2*f(n-2) + f(n)
"""

n = int(input())
dp = [0]*1000
dp[0], dp[1] = 1, 3
for i in range(2,n):
    dp[i] = 2*dp[i-2] + dp[i-1]
print(dp[n-1]%10007)