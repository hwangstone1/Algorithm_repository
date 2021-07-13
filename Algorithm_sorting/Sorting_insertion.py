"""
삽입정렬과 선택정렬 두 정렬방식 모두 timecomplexity 가 O(N^2) 이지만
선택정렬에 비해 실행 시간적인 측면에서 빠르다.
삽입정렬은 어느정도 정렬이 되어있는 리스트에서 더욱 효과적으로 사용된다.
"""


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1], array[j]
        else:
            break
print(array)