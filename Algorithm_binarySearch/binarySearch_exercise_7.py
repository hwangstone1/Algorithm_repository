import sys
input = sys.stdin.readline
n , m = map(int, input().split())
array = [int(input()) for i in range(n)]
start , end = 1, max(array)

while start <= end:
    line = 0
    mid = (start+end)//2

    for i in array:
        line += i//mid
    if line >= m:
        start = mid +1
    else:
        end = mid - 1
print(end)
