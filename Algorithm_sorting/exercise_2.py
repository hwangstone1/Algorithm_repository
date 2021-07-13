"""
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

1.길이가 짧은 것부터
2.길이가 같으면 사전 순으로
"""


n = int(input())
array = []
for i in range(n):
    tmp = input()
    l = len(tmp)
    array.append((tmp,l))
array = set(array)
#lambda 함수는 인자값을 두개도 사용 할수있다.
array = sorted(array, key = lambda name:(name[1],name[0]))

for name in array:
    print(name[0])
