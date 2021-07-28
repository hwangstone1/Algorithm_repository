t = int(input())

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

for _ in range(t):
    array = list(map(int, input().split()))
    n = array[0]
    sum = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i < j:
                sum += gcd(array[i],array[j])
    print(sum)