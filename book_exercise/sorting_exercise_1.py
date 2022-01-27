# 선택정렬

# 순차적으로 가장 작은 원소를 나열

array = list(map(int, input().split()))

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)