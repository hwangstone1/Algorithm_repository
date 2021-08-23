#고정점 찾기

n = int(input())
array = list(map(int, input().split()))

def search_fix(array, start, end):
    if start > end :
        return None
    mid = (start+end)//2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return search_fix(array, start, mid-1)
    else:
        return search_fix(array, mid+1, end)


index = search_fix(array, 0, n-1)
if index == None:
    print(-1)
else:
    print(index)