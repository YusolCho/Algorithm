import sys
input = sys.stdin.readline

n = int(input())
board = [[0] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


for _ in range(n):
    x, y, d, g = map(int, input().split())
    board[x][y] = 1

    curve = [d]
    
    for i in range(g):
        for j in range(len(curve) - 1, -1, -1):
            curve.append((curve[j] + 1) % 4)

    for i in curve:
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 101 and 0 <= ny < 101:
            board[nx][ny] = 1
            x, y = nx, ny

squares = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            squares += 1

print(squares)