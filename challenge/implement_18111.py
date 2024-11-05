
# Answer
# 백준에서 제출할 때 PyPy로 제출 해야함
# dfs, bfs가 아니라 그냥 높이 257까지 모든 경우를 구하는거였다
import sys

n, m, b = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = sys.maxsize
idx = 0

# 0층부터 256층까지 반복
for target in range(257):
    max_target, min_target = 0, 0

    # 반복문을 통해 블록을 확인
    for i in range(n):
        for j in range(m):

            # 블록이 층수보다 더 크면
            if graph[i][j] >= target:
                max_target += graph[i][j] - target

            # 블록이 층수보다 더 작으면
            else:
                min_target += target - graph[i][j]

    # 블록을 뺀 것과 원래 있던 블록의 합과 블록을 더한 값을 비교
    # 블록을 뺀 것과 원래 있던 블록의 합이 더 커야 층을 만들 수 있음.
    if max_target + b >= min_target:
        # 시간 초를 구하고 최저 시간과 비교
        if min_target + (max_target * 2) <= answer:
        	# 0부터 256층까지 비교하므로 업데이트 될수록 고층의 최저시간
            answer = min_target + (max_target * 2) # 최저 시간
            idx = target # 층수

print(answer, idx)

# #1. 상하좌우로 +1, -1을 하면서 모든 원소의 값이 같아졌을때 걸리는 최소의 시간과 땅의 높이
#
# from collections import deque
# n, m, b = map(int, input().split())
# ground = []
# for _ in range(n) :
#     ground.append(list(map(int, input().split())))
#
# visited = [[0]*m for _ in range(n)]
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 0]
#
# def bfs(x,y) :
#     q=deque()
#     q.append((x,y))
#     while q:
#         x, y = q.popleft()
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 :
#