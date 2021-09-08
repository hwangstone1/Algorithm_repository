# 소수의연속합

n = int(input())
array = [False, False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
    if array[i]:
        primes.append(i)
        for j in range(i*2, n+1, i):
            array[j] = False

answer = 0
start = 0
end = 0
while end <= len(primes):
    temp_sum = sum(primes[start:end])
    if temp_sum == n:
        answer += 1
        end += 1
    elif temp_sum < n:
        end += 1
    else:
        start += 1

print(answer)