# 입력의 수가 많아지면 시간제한에 걸리기 때문에
# input 을 sys.stdin.readline 으로 초기화 시켜놓고 사용한다
"""
2차원 평면 위의 점 N개가 주어진다.
좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로
정렬한 다음 출력하는 프로그램을 작성하시오.
"""
import sys
input = sys.stdin.readline
n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
sortarray = sorted(array,key = lambda x : (x[0],x[1]))
for i in sortarray:
    print(i[0],i[1])