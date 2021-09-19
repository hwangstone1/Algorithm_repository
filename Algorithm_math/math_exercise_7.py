#최소공배수

t = int(input())
max_num = 450001


def gcd(a, b):
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b



for _ in range(t):

    x, y = map(int, input().split())
    under_gcd = gcd(x, y)

    result = (x*y)//under_gcd

    print(result)