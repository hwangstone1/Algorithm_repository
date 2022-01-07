# n, m = map(int, input().split())
# result = 0
# for i in range(n):
#     card = list(map(int, input().split()))
#
#     min_value = 10001
#     for k in card:
#         min_value = min(min_value, k)
#
#     result = max(result, min_value)
#
# print(result) 이중구문을 활용한 풀이법

n, m = map(int, input().split())
result = 0
for i in range(n):
    card = list(map(int, input().split()))
    min_value = min(card)
    result = max(result, min_value)
print(result)
