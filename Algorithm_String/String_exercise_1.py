"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다. =>> 대소문자를 구별하지 않기 때문에 대문자와 소문자중 하나로 통일해서 해결
"""
import string
input_list = list(input().upper())
alpha_list = list(string.ascii_uppercase)

tmp_list = [0]*len(alpha_list)
for i in range(len(input_list)):
    for j in range(len(alpha_list)):
        if  input_list[i] == alpha_list[j]:
            tmp_list[j] += 1

M = max(tmp_list)

cnt = 0
for i in range(len(tmp_list)):
    if M == tmp_list[i] :
        cnt += 1

if cnt != 1 :
    print("?")
else:
    for i in range(len(tmp_list)):
        if tmp_list[i] == M:
            print(alpha_list[i])
            break