"""
#병합정렬
병합 정렬은 분할 정복 (Devide and Conquer) 기법과 재귀 알고리즘을 이용해서 정렬 알고리즘입니다.
즉, 주어진 배열을 원소가 하나 밖에 남지 않을 때까지 계속 둘로 쪼갠 후에 
다시 크기 순으로 재배열 하면서 원래 크기의 배열로 합칩니다.
#병합정렬 특징
알고리즘을 큰 그림에서 보면 분할(split) 단계와 방합(merge) 단계로 나눌 수 있으며,
단순히 중간 인덱스를 찾아야 하는 분할 비용보다 모든 값들을 비교해야하는 병합 비용이 큽니다.
예제에서 보이는 것과 같이 8 -> 4 -> 2 -> 1 식으로 전반적인 반복의 수는 점점
절반으로 줄어들기 때문에 O(logN) 시간이 필요하며,
각 패스에서 병합할 때 모든 값들을 비교해야 하므로 O(N) 시간이 소모됩니다. 따라서 총 시간 복잡도는 O(NlogN) 입니다.
두 개의 배열을 병합할 때 병합 결과를 담아 놓을 배열이 추가로 필요합니다. 따라서 공간 복잡도는 O(N) 입니다.
다른 정렬 알고리즘과 달리 인접한 값들 간에 상호 자리 교대(swap)이 일어나지 않습니다.
"""


arr = [1,3,8,5,4,6,2,7]
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))
merge_sort(arr)
print(arr)