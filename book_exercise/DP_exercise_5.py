#바닥공사

n = int(input())

d = [0] * 1001

d[1], d[2] = 1, 3

for i in range(3, n+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 213123213

print(d[n])

