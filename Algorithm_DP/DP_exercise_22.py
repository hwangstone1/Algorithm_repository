# 카드 구매하기 11052
n = int(input())
card_list = [0]
card_list += list(map(int, input().split()))
dp_table = [0]*(n+1)
for i in range(1, n+1):
    for j in range(1, i+1):
        dp_table[i] = max(dp_table[i], dp_table[i-j] + card_list[j])
print(dp_table[i])

