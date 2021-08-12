"""
모든 시리얼 번호는 알파벳 대문자 (A-Z)와 숫자 (0-9)로 이루어져 있다.
시리얼번호 A가 시리얼번호 B의 앞에 오는 경우는 다음과 같다.
A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다.
(숫자인 것만 더한다)
만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
시리얼이 주어졌을 때, 정렬해서 출력하는 프로그램을 작성하시오.
"""

n = int(input()) # 입력개수 n
array = [] # 결과를 저장할 array 선언
for _ in range(n): # 입력수만큼 반복
    tmp = input() # 문자와 숫자가 섞여있으니 문자리스트로 받는다.
    cnt = 0 # 숫자를 저장할 변수를 선언
    for i in tmp: # 입력받은 문자열을 한개의 인자씩 검사
        if i.isdigit(): # 만약 인자가 숫자라면
            cnt += int(i) # 변수에 저장
    array.append((tmp,cnt)) # 문자열과 숫자의 길이를 튜플로 저장
array = sorted(array, key = lambda x : (len(x[0]), x[1], x[0]))
# 차례대로 문자열의 길이 , 숫자의 합 순서 , 사전순으로 정렬

for x in array:
    print(x[0])