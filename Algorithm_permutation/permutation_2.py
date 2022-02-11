
# 순열 알고리즘 구현

# 순열 계산 공식  nP(permutation)r = n!/(n-r)!
# DFS 트리와 체크리스트 사용
# 웬만하면 외우고 있는게 좋음!!


def DFS(L):
    # 종료 조건
    if L == r:
        print(result)
    else:
        for i in range(len(n)):
            if checklist[i] == 0:
                result[L] = n[i]
                checklist[i] = 1
                DFS (L+1)
                checklist[i] = 0



if __name__ == "__main__":
    n = [1, 2, 3]
    r = 2

    result = [0] * r
    checklist = [0] * len(n)

    DFS(0)