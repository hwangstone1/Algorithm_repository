# 30 백준 10610
number = list(input())
number.sort(reverse=True)
result_number = int(''.join(number))
answer = -1
if result_number % 30 == 0:
    answer = result_number
print(answer)