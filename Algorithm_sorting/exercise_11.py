"""
배열을 입력받고 작은순서부터 큰 순서까지 정렬한다.
그다음 0보다 작은 수를 센다 . 홀수일경우 첫번째 인덱스를제외하고
두번째부터 곱해서 더하고
첫번째 인덱스는 더한다.
"""
import sys
input = sys.stdin.readline
n  = int(input())
parray =[]
marray =[]
array = []
allsum = 0
for i in range(n):
    a = int(input())
    if a > 1:
        parray.append(a)
    elif a < 1:
        marray.append(a)
    else:
        array.append(a)
allsum += sum(array)
parray = sorted(parray,reverse = True)
marray = sorted(marray)

if len(parray) % 2 == 0:
    for i in range(0,len(parray)-1,2):
        allsum += parray[i] * parray[i+1]
else:
    for i in range(0,len(parray)-1,2):
        allsum += parray[i] * parray[i+1]
    allsum += parray[-1]
if len(marray) % 2 == 0:
    for i in range(0,len(marray)-1,2):
        allsum += marray[i] * marray[i+1]
else:
    for i in range(0,len(marray)-1,2):
        allsum += marray[i] * marray[i+1]
    allsum += marray[-1]

print(allsum)
