n = int(input())
number = 45
fibo = [0]*(number+1)
fibo[0], fibo[1] = 0, 1

for i in range(2,number+1):
    fibo[i]= fibo[i-1] + fibo[i-2]
print(fibo[n])
print(fibo)