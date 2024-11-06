# Answer.
n, m, x, y, k = map(int, input().split())

board = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for i in range(n):
    board.append(list(map(int, input().split())))

comm = list(map(int, input().split()))

nx, ny = x, y
for i in comm:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[0])


# # 1. 칸에 숫자가 0이 아니라면 칸 -> 주사위 칸=0
# # 2. 숫자가 0이라면 주사위 -> 칸
#
# n, m, x, y, k = map(int, input().split())
# dice = [0, 0, 0, 0, 0, 0]
# graph = []
# for _ in range(n) :
#     graph.append(map(int, input().split()))
#
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
#
# # a e c b d f
# # 오른쪽 => d e a b f c
# # 왼쪽 =>   c e f b a d
# # 아래쪽 => b a c f d e
# # 위쪽 => e f c b d a
#
# def turn(dir) :
#     a,b,c,d,e,f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
#     # 동쪽
#     if dir == 1 :
#         dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, e, a, b, f, c
#     elif dir == 2 :
#         dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, e, f, b, a, d
#     elif dir == 3 :
#         dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, f, c, b, d, a
#     else :
#         dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, a, c, f, d, e
#
# nx, ny = x, y
# move = list(map(int,input().split()))
# for i in move :
#     nx += dx[i-1]
#     ny += dy[i-1]
#
#     if nx<0 or nx >= n or ny < 0 or ny >= m :
#         nx -= dx[i-1]
#         ny -= dy[i-1]
#         continue
#         turn(i)
#         if graph[x][y] == 0 :
#             graph[x][y] = dice[-1]
#         else :
#             dice[-1] = graph[x][y]
#             graph[x][y] = 0
#         print(dice[0])