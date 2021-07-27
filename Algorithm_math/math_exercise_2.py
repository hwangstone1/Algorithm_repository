#숫자 3개가 띄워져서 들어옴
#a,b,c 의 최대공약수를 구한다 예)) 10 , 20 ,30 ->> 10
# a%x = 0 , b%x = 0 , c%x = 0 을 만족시키는 x 를 구해야한다.
# a,b,c 중의 최대(max)값을 구해 최대값까지 x를 증가시킨다

array = list(map(int,input().split()))
M = max(array)
print(M)
tmp = 0
for i in range(1,M+1):
    if array[0]%i == 0 and array[1]%i == 0 and array[2]%i == 0:
        tmp = i
print(tmp)