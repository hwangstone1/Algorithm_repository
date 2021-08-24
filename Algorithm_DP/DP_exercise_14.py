#병사 배치하기
number = int(input())
array = list(map(int, input().split()))
array.reverse()
dp = [1]*number

for i in range(1,number):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(number - max(dp))