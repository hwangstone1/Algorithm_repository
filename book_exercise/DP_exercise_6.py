n , m = map(int, input().split())
money_list = []

for i in range(n):
    money_list.append(int(input()))

d = [10001] * (m+1)
d[0] = 0
for i in range(n): # 화폐의 수만큼
    for j in range(money_list[i], m+1):
        if d[j-money_list[i]] != 10001:
            d[j] = min(d[j], d[j-money_list[i]] + 1)

if d[m] == 10001:
    print(-1)
else : print(d[m])


