n, m = map(int, input().split())
v = m
checklist = [[0]*n for _ in range(n)]
result =[]
idx = 0
def solution(v,checklist,idx):
    if v == m:
        print(' '.join(map(str, result)))
        return
    for i in range(idx,n):
        if checklist[v][i] == 0:
            checklist[v][i] = 1
            result.append(i+1)
            solution(v+1,checklist,i)
            checklist[v][i] = 0
            result.pop()

solution(0,checklist,idx)