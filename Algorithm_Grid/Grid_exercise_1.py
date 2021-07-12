'''
백준 그리드알고리즘 기본
인하은행에는 ATM이 1대밖에 없다.
지금 이 ATM앞에 N명의 사람들이 줄을 서있다.
사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
인하은행에는 ATM이 1대밖에 없다. 지금 이 ATM앞에 N명의 사람들이 줄을 서있다.
줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때,
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.
'''

n = int(input())
jul_list = list(map(int,input().split()))
jul_list = sorted(jul_list)

sum = 0
tmp = 0
if n == 1 :
    print(jul_list[0])

else:
    for i in range(n):
        tmp += (jul_list[i])
        sum +=tmp
        print(sum)
    print(sum)

