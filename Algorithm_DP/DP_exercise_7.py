# 하노이의 탑
n = int(input())

def hanoi(n,l,r): # 시작
    if n == 1:
        print(l,r)
    else:
        hanoi(n-1, l, 6-(l+r))
        print(l, r)
        hanoi(n-1, 6-(l+r), r)

print(2**n-1)
hanoi(n, 1,3)