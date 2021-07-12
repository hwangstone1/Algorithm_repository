"""
이진 검색 알고리즘(binary search algorithm)은 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘이다.
처음 중간의 값을 임의의 값으로 선택하여, 그 값과 찾고자 하는 값의 크고 작음을 비교하는 방식을 채택하고 있다.
처음 선택한 중앙값이 만약 찾는 값보다 크면 그 값은 새로운 최댓값이 되며, 작으면 그 값은 새로운 최솟값이 된다.
검색 원리상 정렬된 리스트에만 사용할 수 있다는 단점이 있지만,
검색이 반복될 때마다 목표값을 찾을 확률은 두 배가 되므로 속도가 빠르다는 장점이 있다.
#반드시 정렬이 된 상태에서 수행해야한다.
"""
'''N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때,
이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
'''

def binary_search(a_list, start, end, target):
    while start<=end: # 대량의 데이터가 들어올때는 재귀보다 반복문이 좋다. 숫자가 커질경우 시간복잡도가 올라간다.
        mid = (start+end)//2
        if a_list[mid] == target:
            return mid
        elif a_list[mid]> target:
            end = mid-1
        elif a_list[mid]< target:
            start = mid+1
        else:
            return None


n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
b_list = list(map(int, input().split()))
a_list = sorted(a_list)


for i in range(m):

    result = binary_search(a_list, 0, n-1, b_list[i])
    if result == None:
        print(0)
    else:
        print(1)
