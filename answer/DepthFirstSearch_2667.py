# Q.
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
#
# Input.
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
# 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
#
# Output.
# 첫 번째 줄에는 총 단지수를 출력하시오.
# 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

# 1. 입력을 이전과는 다르게 2차원에 바로 정수 (0,1)을 입력받게
# 2. bfs?
# 3. 상하좌우에 있는지 확인하고 있을때 탐색을 하면서
# 4. 단지를 카운트,,,
# 5. 순회를 여러번 해야할듯? 끊길때마다 새로 시작하게 됨
# 6. 단지가 끝났는지 어떻게 확인하고 시작하나? -> "탐색을 한 곳은 0으로 바꿔서 다시 방문하지 않게 한다"

from collections import deque

N = int(input())
graph = []
for _ in range(N) :
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y) :
    graph[x][y] = 0
    q=deque()
    q.append((x,y))

    house_cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :
                if graph[nx][ny] == 1 :
                    q.append((nx,ny))
                    graph[nx][ny] = 0
                    house_cnt += 1

    return house_cnt
cnt = []
for j in range(N) : # 어디서 탐색을 시작할지 모르기 때문에 모든 위치를 범위로 잡음
    for k in range(N) :
        if graph[j][k] == 1 : # 탐색을 시작 하려면 집이 있어야 하니 값이 1이어야 함
            cnt.append(bfs(j, k))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])

# dfs 돌리려면 위의 bfs에서 1을 다 0으로 바꿨기 때문에 bfs를 주석 처리하던지 입력을 한 번 더 받아야 함
def dfs(x, y) :
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

cnt2 = []
count = 0
result = 0

for j in range(N) :
    for k in range(N) :
        if dfs(j, k) == True : # 이 구문이 실행되면 전역변수인 count값이 달라져있음
            cnt2.append(count) # 그래서 그 count 값을 리스트에 추가
            result += 1
            count = 0 # 각 단지별 집의 개수를 세어야하기 때문에 다시 초기화

cnt2.sort()
print("dfs : ",result)
for i in range(len(cnt2)) :
    print(cnt2[i])



# num = []
#
#
# def DFS(x, y):
#     if x < 0 or x >= N or y < 0 or y >= N:
#         return False
#
#     if graph[x][y] == 1:
#         global count
#         count += 1
#         graph[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             DFS(nx, ny)
#         return True
#     return False
#
#
# count = 0
# result = 0
#
# for i in range(N):
#     for j in range(N):
#         if DFS(i, j) == True:
#             num.append(count)
#             result += 1
#             count = 0
#
# num.sort()
# print(result)
# for i in range(len(num)):
#     print(num[i])

