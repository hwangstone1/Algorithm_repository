#문자열 재정렬
array = input()
result = []
sum = 0

for i in range(len(array)):
    if array[i].isalpha():
        result.append(array[i])
    else:
        sum += int(array[i])

result = sorted(result)
result.append(str(sum))
print(''.join(result))