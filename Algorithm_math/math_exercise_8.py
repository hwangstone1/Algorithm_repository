# 3036 링
# 첫째줄에 링의 개수가 주어짐
# 다음줄에 링의 반지름이 한개씩 띄어서 주어진다.
# input 2
import sys
input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        remain = a%b
        a = b
        b = remain
    return a

n = int(input())
half = list(map(int, input().split()))

target = half.pop(0)

for i in range(n-1):
    num = gcd(target, half[i])

    print('{}/{}'.format(target//num, half[i]//num))