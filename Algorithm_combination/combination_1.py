
# 조합 알고리즘 구현

# 조합 계산 공식  nC(combination)r = nPr/r!
# DFS 트리와 트래버스할 때 다음시작점을 가지고 감
# 웬만하면 외우고 있는게 좋음!!

def DFS(L, BeginWidth):

    # 종료 조건
    if L == r :
        print(result)
    else:
        for i in range(BeginWidth, len(n)):
            result[L] = n[i]
            DFS(L+1, i+1)



if __name__ == "__main__":
    # nCr

    n = [1, 2, 3]
    r = 2

    result = [0] * r
    DFS(0, 0) # 0 Level , 0 Beginwidth