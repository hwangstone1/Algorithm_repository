"""
숫자 카드는 정수 하나가 적혀져 있는 카드이다.
상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
"""

n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))
N = sorted(N)
def binary(array, i, start, end):
    while (start <= end):
        mid = (start+end)//2
        if i == array[mid]:
            return 1
        elif i < array[mid]:
            end = mid-1
        else:
            start = mid+1

for i in M:
    result = binary(N, i, 0, n-1)
    if result == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')