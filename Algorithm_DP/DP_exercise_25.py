# DP 동전 1

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
dp = [0] * 10000
for _ in range(n):
    money = int(input())
    arr.append(money)
    dp[money] += 1
print(arr)
for i in range(n):
    print(dp[i],end='')