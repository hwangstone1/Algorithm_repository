def backt(x, y, word):
    global result
    check = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and words[nx][ny] not in word:  # 인덱스 초과 방지 & 문자 중복 방지
            backt(nx, ny, word+words[nx][ny])
        else:
            check += 1


    if check == 4:
        result = max(result, len(word))
        return


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
words = [list(input()) for _ in range(n)]
result = 0
backt(0, 0, words[0][0])
print(result)