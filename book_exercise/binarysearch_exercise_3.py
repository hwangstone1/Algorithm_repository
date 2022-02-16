n, m = map(int, input().split(' '))
ricecake = list(map(int, input().split()))

low , high = 0, max(ricecake)
result = 0

while low <= high:
    total = 0
    mid = (low + high) // 2
    for i in ricecake:
        if i > mid:
            total += i - mid
    if total > m:
        low = mid + 1
    else:
        result = mid
        high = mid - 1
print(result)