# 별찍기

n = int(input())

for i in range(1,(2*n)):
    if (i<=n):
        for j in range(n-i):
            print(' ', end='')

        for j in range(i):
            print('*', end='')
        print('')
    else:
        for j in range(i-n):
            print(' ', end='')
        for j in range((n*2)-i):
            print('*', end='')
        print('')

