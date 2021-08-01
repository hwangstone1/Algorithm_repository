t = int(input())
array = [0]*12
array[1], array[2], array[3] = 1, 2, 4
def solution(n):
    for i in range(4,n+1):
        array[i] = array[i-3] + array[i-2] + array[i-1]

for _ in range(t):
    n = int(input())
    solution(n)
    print(array[n])