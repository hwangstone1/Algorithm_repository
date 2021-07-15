"""
공백이 포함된 문자열이 들어왔을때 , 문자열안의 단어의 개수를 출력하는 문제
공백이 포함된 문자열은 split() 으로 공백을 기준으로 단어를 입력 받을수있다 .
"""

input_data = input().split()
print(len(input_data))