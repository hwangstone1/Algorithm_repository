"""
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

"""


n = int(input())

result = n

for i in range(0,n):
    tmp = input()
    for j in range(0, len(tmp)-1):
        if tmp[j] == tmp[j+1]: # 단어의 [j]번째와 [j+1]번째가 같으면 다음 인덱스로 넘어감
            continue
        elif tmp[j] in tmp[j+1:]: # if 조건 ( [j] 번째와 [j+1] 번째가 같다) 만족하지 않으면 , 확인이된 문자 뒤로 또 문자가있는지
            result -= 1           # 슬라이싱 [시작위치:끝위치] 를 통해 확인한다.
            break
print(result)
