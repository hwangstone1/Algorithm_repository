# ### bottom-up 방식
#
#
# def bottomup():
#     n = int(input())
#
#     d = [0] * (n+1)
#
#     d[1], d[2] = 1, 1
#
#     for i in range(3, n+1):
#         d[i] = d[i-1] + d[i-2]
#         print(d[i])
#
#     print(d[n])
#

### top-down 방식



d = [0] * 100


def fibo(x):

    if x == 1 or x == 2 :
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)

    return d[x]


n = int(input())
print(fibo(n))

