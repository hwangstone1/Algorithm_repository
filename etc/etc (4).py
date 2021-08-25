#요세푸스 문제

n, k = map(int, input().split())
array =[]
result = []
for i in range(1, n+1):
    array.append(i)
print(array)
target = k-1
while len(array):

    if target >= len(array):
        target = target % len(array)
    else:
        result.append(str(array.pop(target)))
        target += k-1

print("<", ", ".join(result), ">", sep='')

