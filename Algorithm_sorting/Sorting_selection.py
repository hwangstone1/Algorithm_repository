"""
데이터가 무작위로 여러개 있을때, 이중에서 가장작은 데이터를 선택해
맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서
두 번째 데이터와 바꾸는 과정을 반복하는 정렬기법

"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    tmp = array[i]
    array[i] = array[min_index]
    array[min_index] = tmp  # 스와프 과정
    # python 스와프 간소화 = a,b = b , a ex) array[i],array[min_index] = array[min_index],array[i]
print(array)