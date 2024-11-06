import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]
r,c,d = map(int,input().split())

# d => 0,3,2,1 순서로 돌아야한다.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 처음 시작하는 곳 방문 처리
visited[r][c] = 1
cnt = 1

while 1:
    flag = 0
    # 4방향 확인
    for _ in range(4):
        # 0,3,2,1 순서 만들어주기위한 식
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        # 한번 돌았으면 그 방향으로 작업시작
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                #청소 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break
    if flag == 0: # 4방향 모두 청소가 되어 있을 때,
        if graph[r-dx[d]][c-dy[d]] == 1: #후진했는데 벽
            print(cnt)
            break
        else:
            r,c = r-dx[d],c-dy[d]

# # 1. dfs?
# # 2. 청소됐을떄와 안됐을때 나눠서 돌려야할듯
#
# n, m = map(int, input().split())
# fx, fy, fdir = map(int, input().split())
# graph = []
# for _ in range(n) :
#     graph.append(list(map(int,input().split())))
#
# visited = [[False] * m for _ in range(n)]
#
# def dfs(x,y, dir) :
#     dx = [0, 0, 1, -1]
#     dy = [1, 1, 0, -1]
#
#     for i in range(4) :
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 :
#             if graph[nx][ny] == 0 : # 청소되지 않은 빈칸이 있는 경우
#                 # 동서남북에 따라 case 문?
#                 if dir == 0 :
#                     dfs(nx)
#                 elif dir == 1 :
#                 elif dir == 2 :
#                 elif dir == 3 :
#
#                 visited[nx][ny] = 1
#                 dfs(nx, ny, dir)
#                 graph[nx][ny] = 2
#                 visited[nx][ny] = 0
#         elif 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 1 :
#             if graph[nx]
