# 알고리즘 선택은 좋았지만 dfs만으로 풀 수있진 않음. -> T자 모양을 참색할 수 없음
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = -1


def DFS(L, x, y, total):
    global answer
    if L == 4:
        answer = max(answer, total)
    elif (total+max_value*(4-L)) <= answer: # 변경점2
        return
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < N and 0 <= yy < M and ch[xx][yy] == 0:
                ch[xx][yy] = 1
                if L == 2: # 변경점 1
                    DFS(L+1, x, y, total+board[xx][yy])
                DFS(L+1, xx, yy, total+board[xx][yy])
                ch[xx][yy] = 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ch = [[0]*M for _ in range(N)]
    max_value = max(map(max, board)) # 변경점2

    for i in range(0, N):
        for j in range(0, M):
            ch[i][j] = 1
            DFS(1, i, j, board[i][j])
            ch[i][j] = 0

    print(answer)


# 1. 테트로미노 5개라 케이스 5개
# 2. 각 케이스마다 회전, 대칭의 경우의 수 추가
# 근데 어짜피 연결된 4개를 선택하면 저 5개 중 하나가 나올듯?
# 결국엔 이웃한 4개의 숫자를 선택해서 최대의 합으로 만드는 문제인듯

# from collections import deque
# n, m = map(int, input().split())
# graph = []
# for _ in range(n) :
#     graph.append(list(map(int, input().split())))
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# visited = [[0]*m for _ in range(n)]
# def bfs(x,y) :
#     q = deque()
#     q.append((x,y))
#     tetromino = []
#     tetromino.append((x,y))
#     while q :
#         if len(tetromino) == 4 : break
#         x, y = q.popleft()
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != 1 :
#                 visited[nx][ny] = 1
#                 q.append((nx,ny))
#                 tetromino.append((nx,ny))
#                 visited[nx][ny] = 0
#
#     return tetromino
#
# visited2 = [[0]*m for _ in range(n)]
# def dfs(x,y,tetromino) :
#     global total
#     if len(tetromino) == 4 :
#         return tetromino
#
#     for i in range(4) :
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m and visited2[nx][ny] == 0 :
#             visited2[nx][ny] = 1
#             tetromino.append((nx,ny))
#             dfs(nx,ny,tetromino)
#             visited2[nx][ny] = 0
#
#
# max_total = 0
# for j in range(n) :
#     for k in range(m) :
#         tetrominoes = dfs(j,k,[(j,k)])
#         if len(tetrominoes) == 4 :
#             total = sum(tetrominoes)
#             if max_total < total :
#                 max_total = total
#
# print(max_total)
#
#


