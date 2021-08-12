n = int(input())
array = list(map(int, input().split()))
x = int(input())
sortarray = sorted(array)
left, right = 0, n-1
sum = 0
count = 0

while left < right:
    sum = sortarray[left] + sortarray[right]
    if sum == x:
        count += 1
    if sum < x :
        left += 1
        continue
    right -= 1
print(count)