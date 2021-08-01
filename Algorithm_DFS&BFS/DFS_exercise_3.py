# 테스트 케이스는 여러가지  0,0 이 입력되면 종료
# 입력 첫줄에 w,h 가로와 높이가 주어진다.
# w , h 크기의 배열을 생성하고 섬의 정보를 입력받는다 .
# 똑같은 크기에 방문했는지 안했는지 알수있는 check 테이블을 만들어준다 .
# 지도를 돌며 방문하며 섬이고 , 동시에 방문하지 않은 섬이라면 dfs 를 통해
# 한섬에 이어진 모든 경로를 체크한다 .
# 한섬에 이어진 가로, 세로, 대각선의 방향으로 체크한뒤 섬이면 이어진섬을 재귀적으로 계속 호출한다.
# 열은 w 이고 행은 h 이다.
import sys
sys.setrecursionlimit(1000)

def dfs(x, y, array, check):
    check[x][y] = 1
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if array[nx][ny] == 1 and check[nx][ny] == 0:
                dfs(nx, ny, array, check)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break
    array = [list(map(int, input().split())) for _ in range(h)]
    check = [[0]*w for _ in range(h)]
    cnt = 0
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    for i in range(h):
        for j in range(w):
            if check[i][j] == 0 and array[i][j] == 1:
                dfs(i,j,array,check)
                cnt += 1
    print(cnt)