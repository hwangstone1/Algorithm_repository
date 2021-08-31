"""
# 수들의 합 2
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
"""
n, m = map(int, input().split())
array = list(map(int, input().split()))

result = 0
end = 0
summary = 0
for start in range(n):
    while summary < m and end < n:
        summary += array[end]
        end += 1

    if summary == m:
        result += 1
    summary -= array[start]
print(result)
