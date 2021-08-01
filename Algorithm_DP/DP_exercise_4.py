# 2*n 타일링
n = int(input())
array = [1,2]

def f(n):
    for i in range(2,n):
        array.append((array[i-1]+array[i-2])%10007)
f(n)
print(array[n-1])