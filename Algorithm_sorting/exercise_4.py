"""
일직선상의 마을에 여러 채의 집이 위치, 특정위치의 한집에 한개의 안테나 설치
안테나로 부터 모든 집까지의 거리가 최소가 되는 안테나를 설치할 위치를 반환하는 프로그램을 작성하시오.
동일 값이 있을땐 작은 값을 출력한다.
## 내가 혼자서 푼 풀이
n = int(input())
home_list = list(map(int, input().split()))
tmp_list = []
for i in home_list:
    result = 0
    for j in range(len(home_list)):
        if i >= home_list[j]:
            result += i - home_list[j]
        else:
            result += home_list[j]-i
    tmp_list.append(result)
print(tmp_list)
max = 100000
cnt = 0
for i in range(len(tmp_list)):

    if tmp_list[i] < max:
        max = tmp_list[i]
        cnt = i
print(home_list[cnt])
"""
# 정답 (이렇게 풀까 생각도 했지만 증명을 못해서 시도하지 않았다 ..)
n = int(input())
an_list = list(map(int, input().split()))
an_list = sorted(an_list)

print(an_list[(n-1)//2])