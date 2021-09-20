# 단어 뒤집기
t = int(input())

for _ in range(t):
    string = input().split()
    result = ""

    for i in string:
        for j in range(len(i)-1,-1, -1):
            result += i[j]
        result += " "

    print(result)