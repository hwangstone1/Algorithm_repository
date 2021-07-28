"""
두정서 a, b 가 주어졌을때 두수의 최대공약수(GCD)를 구하시오.
"""
n , m = map(int, input().split())


def gcd(x,y):
    if x < y:
        x, y = y, x
    elif x % y == 0:
        return y
    else:
        return gcd(y,x % y)

print(gcd(n, m))