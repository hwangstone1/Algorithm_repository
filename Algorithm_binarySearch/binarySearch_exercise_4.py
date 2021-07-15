"""
1.두배열을 입력받고, 포문에서 인덱스를 빼서 함수로 돌려준다.
2.비교 array[인덱스]가 존재하면 1을 반환후 결과값 배열 array[인덱스]를 1증가시킨다.
"""
n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))
array3 = [0]*m
print(array3)
array = sorted(array1)


def binary(a, x, start, end):
    while(start <= end):
        mid = (start+end)//2
        if a[mid] == array2[x]:
            return 1
        elif a[mid] < array2[x]:
            start = mid+1
        else:
            end = mid-1
    return None
for i in range(m):

    result = binary(array, i, 0, n-1)
    if result == 1 :
        array3[i] += 1
print(array3)
