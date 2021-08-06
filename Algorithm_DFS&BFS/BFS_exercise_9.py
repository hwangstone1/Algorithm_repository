from collections import deque
n, k = map(int, input().split())

def bfs(n,k):
    number = 100001
    array = [0]*number
    q = deque()
    q.append(n)
    dx = [-1, 1, 2]
    while q:
        x = q.popleft()

        if x == k:
            print(array[x])
            return

        for i in dx:
            if i == 2:
                newx = x*i
                if 0 <= newx < number and array[newx] == 0:
                    array[newx] = array[x]
                    q.append(newx)
            else:
                newx = x+i
                if 0 <= newx < number and array[newx] == 0:
                    array[newx] = array[x] + 1
                    q.append(newx)
    print(array[k])
    return

bfs(n, k)