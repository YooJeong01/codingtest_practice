# 1. bfs로 큐에 담아두고 -> 같은 종류만 탐색되니까,,,
# 2. bfs의 값이 R/Y/G인 경우로 따로 돌려야 할듯
# 3. 그리고 세개를 돌린 후에 한 번에 비우기 연쇄 + 1
# 4. 예를 들어 큐에 R4 G4라면 R과 G모두 동시에 비움 -> 연쇄 +=1
# 연쇄가 일어나고나면 터지지 못하고 큐에 남아있는 것도 자리가 바뀌므로 큐는 통째로 비우기..?
# 5. 터진 자리는 . 으로 바꾸고
# 6. 뿌요 밑으로 .이 존재한다면 . 갯수만큼 x(행)값 증가해서 이동시켜주기
#
# 7. 다시 bfs 돌리기
# 8. 몇 연쇄가 됐는지 출력하기

# Answer
# 뿌요 내리기 부분 이해 필요!
import sys
from collections import deque
input = sys.stdin.readline


def check(x, y):
    q = deque([(x, y)])
    now = graph[x][y]
    pos = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and graph[nx][ny] == now and not visited[nx][ny]:
                pos.append((nx, ny))
                q.append((nx, ny))
                visited[nx][ny] = 1

    if len(pos) >= 4:
        pos.sort(key=lambda x: (x[1], x[0]))
        for i, j in pos:
            graph[i][j] = '_'
            bombList.append((i, j))


graph = [list(input().rstrip()) for i in range(12)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0

while True:
    visited = [[0] * 6 for _ in range(12)]
    bombList = []

    # 색이 같은 뿌요 4개 이상 모여있는 곳 있는지 체크해서 터뜨리기
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and graph[i][j] != '_' and not visited[i][j]:
                check(i, j)

    if len(bombList) == 0:
        break

    # 뿌요 내리기
    for bomb in bombList:
        x, y = bomb[0], bomb[1]
        for i in range(x, 0, -1):
            graph[i][y] = graph[i-1][y]
        graph[0][y] = '.'

    time += 1

print(time)

# from collections import deque
# field = []
# for _ in range(12) :
#     field.append(list(map(str,input().split())))
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def bfs(x,y) :
#     cnt = 0
#     q = deque()
#     bomb = deque([])
#     while q:
#         x, y = q.popleft()
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if field[x][y] == field[nx][ny] and not visited[nx][ny] and 0 <= nx < 12 and 0 <= ny < 6:
#                 visited[nx][ny] = True
#                 q.append((nx,ny))
#                 bomb.append((nx,ny))
#                 cnt += 1
#     if cnt >= 4 :
#         bomb.sort(key=lambda x: (x[1], x[0]))
#         for i, j in bomb:
#             field[i][j] = '_'
#             bombList.append((i,j))
#
#
#
# time = 0
# while True :
#     visited = [[0]*6 for _ in range(12)]
#     bombList = []
#
#     for i in range(12) :
#         for j in range(6) :
#             if field[i][j] != '.' and field[i][j] != '_' and not visited[i][j] :
#                 bfs(i,j)
#
#     if len(bombList) == 0 :
#         break
#
#     for b in bombList :
#         x, y = b[0], b[1]
#         for i in range(x, 0, -1) :
#             field[i][y] = field[i-1][y]
#         field[0][y] = '.'
#
#     time += 1
#
# print(time)

# from collections import deque
# field = []
# for _ in range(12) :
#     field.append(list(map(str,input().split())))
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def bfs(x,y) :
#     cnt = 0
#     q = deque()
#     bomb = deque([])
#     while q:
#         x, y = q.popleft()
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if field[x][y] == field[nx][ny] and not visited[nx][ny] and 0 <= nx < 12 and 0 <= ny < 6:
#                 visited[nx][ny] = True
#                 q.append((nx,ny))
#                 bomb.append((nx,ny))
#                 cnt += 1
#     return cnt
#
# flag = 0
# crush = 0
# for j in range(11, 1, -1) :
#     for k in range(6) :
#         visited = [[False] * 6 for _ in range(12)]
#         if field[j][k] == "R" :
#             cnt = bfs(j, k)
#             if cnt >= 4 :
#                 flag = 1
#         elif field[j][k] == "Y" :
#             cnt = bfs(j, k)
#             if cnt >= 4 :
#                 flag = 1
#         elif field[j][k] == "G" :
#             cnt = bfs(j, k)
#             if cnt >= 4 :
#                 flag = 1
#         if flag == 1 :
#             crush += 1



