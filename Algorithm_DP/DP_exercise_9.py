# 1로만들기

n = int(input())

array = [0]*10**6

for i in range(2,n+1):
    array[i] = array[i-1] + 1
    if i % 2 == 0: # i가 2로 나누어 떨어질때
        array[i] = min(array[i], array[i//2]+1)# 2로 나누었을때 그숫자의 연산횟수 + 1을해줘서 현재 d[i]랑 비교한다
    if i % 3 == 0: # i 가 3으로 나누어 떨어질때
        array[i] = min(array[i], array[i//3]+1)# 3으로 나누었을때 그숫자의 연산횟수 + 1을해줘서 현재 d[i]랑 비교한다

print(array[n])
