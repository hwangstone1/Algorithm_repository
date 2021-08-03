#중복허용
n, m = map(int, input().split())
v = m
checklist = [[0]*n for _ in range(n)]
result =[]
def solution(v,checklist):
    if v == m:
        print(' '.join(map(str, result)))
        return
    for i in range(n):
        if checklist[v][i] == 0:
            checklist[v][i] = 1
            result.append(i+1)
            solution(v+1,checklist)
            checklist[v][i] = 0
            result.pop()

solution(0,checklist)