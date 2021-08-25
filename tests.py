import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
array = sorted(array)
mid = len(array)//2-1
print(array[mid])