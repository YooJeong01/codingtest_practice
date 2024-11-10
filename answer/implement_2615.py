# 가로, 세로, 대각선으로 좌표를 이동해보면서
# 같은게 있으면 cnt 증가
# 끊기면 재귀 탈출 및 cnt 리턴
# cnt값이 5면 걔가 승리
# 좌표값이 오목판 내에 유효한 좌표인지 확인

# Answer.
import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
move= [[1,0],[1,1],[0,1],[-1,1]]
N = 19
result = 0

for i in range(N):
    for j in range(N):
        if board[i][j] != 0: # 돌이 있는 칸이면
            stone = board[i][j] # 돌의 색 저장
            for dy, dx in move:
                ny, nx, cnt = i + dy, j + dx, 1
                while 0 <= ny < N and 0 <= nx < N and board[ny][nx] == stone: # 범위내에 있고, 해당 방향에 돌 색이 있다면
                    cnt += 1 # 1개씩 증가
                    if cnt == 5: # 오목이 됐으나 육목 체크
                        if 0 <= i - dy < N and 0 <= j - dx < N and board[i-dy][j-dx] == stone: # 반대칸에 하나 더 있거나
                            break
                        if 0 <= ny + dy < N and 0 <= nx + dx < N and board[ny+dy][nx+dx] == stone: # 앞에 한칸에 더 있으면
                            break
                        if stone == 1: # 흑돌
                            result = 1
                        if stone == 2: # 백돌
                            result = 2
                        y, x = i, j
                    ny += dy # 해당 방향으로 전진 해보자
                    nx += dx # 해당 방향으로 전진 해보자
if result > 0:
    print(result)
    print(y+1,x+1)
else:
    print(0)





# omok = []
# for _ in range(19) :
#     omok.append(list(map(int, input().split())))
#
# dx = [-1, 1, 0, 0, -1, -1, 1, 1]
# dy = [0, 0, -1, 1, -1, 1, -1, 1]
#
# visited = [[False]*19 for _ in range(19)]
# def dfs(x,y,cnt) :
#     if cnt >= 5 :
#         return cnt
#     for i in range(8) :
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if not visited[nx][ny] and omok[x][y] == omok[nx][ny] and 0 <= nx < 19 and 0 <= ny < 19 :
#             visited[nx][ny] = True
#             item.append((nx,ny))
#             cnt += 1
#             dfs(nx, ny, cnt)
#             visited[nx][ny] = False
#
# for j in range(19) :
#     for k in range(19) :
#         if omok[j][k] != 0 :
#             visited[j][k] = True
#             item.append((j,k))
#             cnt = dfs(j, k,0)
#             if cnt == 5 :
#                 if omok[j][k] == 1 :
#                     print(1)
#                     print(item.pop(0))
#                 else :
#                     print(2)
#                     print(item.pop(0))
#             else : print(0)

