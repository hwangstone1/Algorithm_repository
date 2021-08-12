n = int(input())
array = list(map(int, input().split()))
array.sort()
count = 0
group = 0

for i in array:
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group)
