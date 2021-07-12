'''
나무의수 N 가져가야할 나무의 총 미터 M 절단기의 최대높이 h
'''
n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))
array = sorted(array)

start = 0
end = max(array)
total = 0
while (start <= end):
    sum = 0
    mid = (start+end)//2
    for i in array:
        if i> mid:
            sum+= i-mid

    if sum < m:
        end = mid-1
    else:
        total = mid
        start = mid+1

print(total)