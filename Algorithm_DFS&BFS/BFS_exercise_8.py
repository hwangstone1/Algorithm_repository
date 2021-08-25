from collections import deque
# 수빈이와 동생의 위치를 받음
n, k = map(int, input().split())
def bfs(n, k):
    if n >= k : # 수빈이가 동생보다 멀리있을경우
        print(n-k) # -1 씩 이동한다
        print(1)
        return
    number = 100001
    result = []
    check = [0]*number
    q = deque([(n,0)]) # 일단 수빈이의 위치와 이동횟수를 큐에 넣고 시작
    count = 0 # 수빈이가 동생의 위치까지 갈수있는 방법의 수
    while q: # q가 빌때까지 모든경로를 탐사할때까지
        x, cnt = q.popleft()
        if x == k : # 수빈이가 동생의 위치까지 왔을때
            if check[x] == 0 :
                check[x] = cnt
                count += 1
            else:
                if cnt == check[x]:
                    count += 1
            result.append(check[x])
        for i in (x-1, x+1, x*2):

            if  0 <= i < number:
                if check[i] == 0 or check[i] >= cnt + 1:
                    if check[k] and cnt + 1 > check[i]:
                        continue
                    check[i] = cnt + 1
                    q.append((i,cnt+1))
    print(check[x])
    print(count)
    print(result)
    return

bfs(n, k)