#test case 123402 7755
# 럭키 스트레이트
n = input()
lsum, rsum = 0, 0

for i in range(len(n)):
    if i < (len(n)//2):
        lsum += int(n[i])
    else:
        rsum += int(n[i])

if lsum == rsum:
    print('LUCKY')
else:
    print('READY')