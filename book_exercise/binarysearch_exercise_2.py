# import sys
#
# n = sys.stdin.readline().rstrip()
# arr_1 = list(map(int, input().split()))
# m = int(input())
# arr_2 = list(map(int, input().split()))
#
# arr_1 = sorted(arr_1)
# result_arr = []
#
#
# def bi(arr, target, low, high):
#     mid = (low + high) // 2
#     if low > high:
#         return "no"
#     if arr[mid] > target:
#         return bi(arr, target, low, mid-1)
#     elif arr[mid] < target:
#         return bi(arr, target, mid+1, high)
#     else:
#         return "yes"
#
# for i in range(m):
#     result = bi(arr_1,arr_2[i], 0, len(arr_1)-1)
#     result_arr.append(result)
#
# for i in range(m):
#     print(result_arr[i], end=' ')


def bi(array, target, low, high):
    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        return None


n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = bi(array, i, 0, len(array)-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end= ' ')

"""
계수정렬
array = [0] * 10000
n = int(input())
for i in input().split():
    array[int(i)] = 1
    
m = int(input())
x = list(map(int, input().split())

for i in x:
    if array[i] == 1:
        print("yes", end=' ')
    else:
        print("no", end = ' ')
        
# 집합형 set 이용

n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
"""