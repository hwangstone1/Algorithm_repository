"""
삽입정렬은 다른 정렬에 비해 속도가 느린편이다.
선택정렬에 비해 효율적이다.
삽입정렬은 특정한 데이터를 적절한 위치에 삽입한다
삽입정렬의 timecomplexity = O(n2) 선택정렬과 비슷
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(array)):

    for j in range(i,0,-1):
        if array[j]<array[j-1]: # 한 개의 원소를 적절한 위치에 놓을때까지 진행한다.
            array[j],array[j-1] = array[j-1],array[j]
        else:
            break
print(array)