# Answer
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
virus = []
for i in range(n) :
    graph.append(list(map(int, input().split())))
    for j in range(n) :
        if graph[i][j] != 0 :
            virus.append((graph[i][j], 0, i, j)) # 바이러스의 종류, 시간, x, y 좌표 전달
virus.sort() # 작은것부터 정렬

q = deque(virus)

target_time, target_x, target_y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

while q :
    virus, t, x, y = q.popleft()
    if t == target_time :
        break
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n :
            if graph[nx][ny] == 0 :
                graph[nx][ny] = virus
                q.append((virus, t+1, nx, ny))

print(graph[target_x - 1][target_y - 1])

# n, k = map(int, input().split())
# virus = []
# for _ in range(n) :
#     virus.append(list(map(int, input().split())))
#
# max_num, min_num = virus[0][0], virus[0][0]
# for j in range(n) :
#     for k in range(n) :
#         if max_num < virus[j][k] :
#             max_num = virus[j][k]
#         if min_num > virus[j][k] :
#             min_num = virus[j][k]
#
# # 1. 큰 수 부터 칸이 0 이거나 칸에 들어있는수가 자신보다 크다면 확산 (상하좌우로만)
# # 2. 리스트의 가장 작은 값을 구하고, 가장 작으값까지 for문이 다 돌면 1초 지남
# # Answer : 바이러스 정보를 q에 저장해서 꺼내 쓰자!
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
#
# visited = [[0]*n for _ in range(n)]
#
# def dfs(x, y) :
#     for j in range(4) :
#         nx = x + dx[j]
#         ny = y + dy[j]
#         if not visited[nx][ny] and 0 <= nx <  n and 0 <= ny < n :
#             visited[nx][ny] = 1
#             if virus[nx][ny] == 0 or virus[nx][ny] > virus[x][y] :
#                 virus[nx][ny] = virus[x][y]
#                 dfs(nx, ny)
#             visited[nx][ny] = 0





