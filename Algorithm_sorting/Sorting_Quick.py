"""
분할 정복 알고리즘의 하나, 평균적으로 매우 빠른 수행 속도를 자랑하는 정렬 방법.
퀵정렬의 timecomplexity = O(NlogN) 으로 매우빠르다.
"""
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(array,start,end):
    if start >= end :
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:

        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quick(array, start, right-1)
    quick(array, right+1, end)



quick(array,0,len(array)-1)
print(array)