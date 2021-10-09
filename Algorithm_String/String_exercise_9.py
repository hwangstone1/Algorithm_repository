# 문자열분석
import string
import sys
alpa = string.ascii_lowercase
ALPA = string.ascii_uppercase
number = []
for i in range(10):
    number += str(i)



while True:
    array = sys.stdin.readline().rstrip('\n')
    if not array:
        break
    al , AL, num, sp = 0, 0, 0, 0

    for i in range(len(array)):
        if array[i] in number:
            num +=1
        elif array[i] in ALPA:
            AL +=1
        elif array[i] in alpa:
            al +=1
        else:
            sp +=1
    sys.stdout.write("{} {} {} {}\n".format(al, AL, num, sp))
