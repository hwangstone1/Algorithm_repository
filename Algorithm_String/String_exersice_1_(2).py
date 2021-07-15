"""
문자열 문제를 풀때는 파이썬의 문법의 도움을 받는것이 매우 효율적이고 쉽게 해결할수있다.
upper , lower 함수로 대문자 , 소문자를 통일할수있고 ,
count , index  x.count(i) , index(i) 를 통해 개수와 인덱스번호를 알아낼수 있다 .
"""
input_data = list(input().upper())
tmp_data = list(set(input_data))

cnt = []
for i in tmp_data:
    count = input_data.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) != 1:
    print('?')
else:
    print(tmp_data[(cnt.index(max(cnt)))])