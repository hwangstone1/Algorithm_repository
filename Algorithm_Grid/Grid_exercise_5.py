# 만들 수 없는 금액
n = int(input())
array =  list(map(int, input().split()))
array = sorted(array) # 어레이를 오름차순으로 정렬
target = 1 # 1원부터 타겟을 증가시키며 만들수 있는지 없는지 확인

for i in array: # array 에 있는 동전의 정보를 하나씩뺌
    if target < i : # 가지고 있는 동전이 만들수있는 돈 보다 크면
        break # target 은 만들지 못하는 동전이므로 멈춤
    target += i # 만들수 있는 경우에는 타겟을 더해줌

print(target)

