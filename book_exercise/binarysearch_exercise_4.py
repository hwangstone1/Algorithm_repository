# 백준 나무자르기 이분탐색

n, m = map(int ,input().split())
tree = list(map(int, input().split()))

low , high = 1, max(tree)
while low <= high:
    mid = (low + high) // 2
    total = 0
    for i in tree:
        if i > mid:
            total += i - mid
    if total >= m:
        low = mid + 1
    else:
        high = mid - 1
print(high)