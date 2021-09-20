# ROT13
# 영어 알파벳을 13자리씩 밀어서 만든 새로운 문자열
import string
import math

al = string.ascii_lowercase
AL = string.ascii_uppercase

print(al)
strr = input()
print(len(al), len(AL))
resultstr = ""

for i in range(len(strr)):

    if strr[i] in al:
        tmp = al.index(strr[i])
        length = len(al)
        if tmp + 13 >= length:
            resultstr += al[abs(length-(tmp+13))]
        else:
            resultstr += al[tmp+13]

    elif strr[i] in AL:
        tmp = AL.index(strr[i])
        length = len(AL)
        if tmp + 13 >= length:
            resultstr += AL[abs(length-(tmp+13))]
        else:
            resultstr += AL[tmp+13]
    else:
        resultstr += strr[i]

print(resultstr)
