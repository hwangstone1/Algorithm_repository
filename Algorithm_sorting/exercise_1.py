"""
입력받은 수만큼 이름과 나이 정보를 받아
나이순대로 정렬하시오.
"""

n = int(input())
array = []
for i in range(n):
    tmp = input().split()
    array.append((int(tmp[0]),tmp[1]))

array = sorted(array,key=lambda x:x[0])

for x in array:
    print(x[0],x[1])