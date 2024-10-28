# Q.
# 차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다.
# 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에,
# 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다.
# 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다.
# 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면
# 이 지렁이는 인접한 다른 배추로 이동할 수 있어,
# 그 배추들 역시 해충으로부터 보호받을 수 있다.
# 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.
#
# 한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다.
# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로
# 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면
# 총 몇 마리의 지렁이가 필요한지 알 수 있다.
# 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.
# 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.
#
# 1 1 0 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 0
# 0 0 1 1 0 0 0 1 1 1
# 0 0 0 0 1 0 0 1 1 1
#
# Input.
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
# 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는
# 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50),
# 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다.
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.
# 두 배추의 위치가 같은 경우는 없다.
#
# Output.
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

# 예제에서 최소 5마리의 배추흰지렁이가 필요하다고 한거보면 구역의 수를 정하는 느낌으로 풀면 될 듯?


# T: 테스트 케이스 개수
# M: 가로 길이
# N: 세로 길이
# K: 배추가 심어진 위치의 개수

# 재귀로 풀게된다면 파이썬에서는 반드시 이 헤더 2줄을 포함해야 함!! 특히 코테의 경우!!
import sys
sys.setrecursionlimit(10000)


# 왜 내 코드는 인덱스 범위 오류가 나는지 분석해봐야 할 듯
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# 
# visited를 따로 쓰는게 나은가? 아니면 graph에서 바로 바꾸는게 나은가?
# def dfs(x,y) :
#     graph[x][y] = 0
#
#     for i in range(4) :
#         nx = x + dx
#         ny = y + dy
#         if 0 <= nx < N and 0 <= ny < M :
#             if graph[nx][ny] == 1 :
#                 dfs(nx,ny)
#
# T = int(input())
#
# for _ in range(T) :
#     M, N, K = map(int, input().split())
#     graph = [[0]*M for _ in range(N)]
#     cnt = 0
#
#     for _ in range(K) :
#         x, y = map(int,input().split())
#         graph[x][y] = 1
#
#     for j in range(N) :
#         for k in range(M) :
#             if graph[j][k] == 1 :
#                 dfs(j,k)
#                 cnt += 1
#                 print(cnt)

T = int(sys.stdin.readline()) # 테스트 케이스 받는 부분

dx = [-1, 1, 0, 0] # 상하좌우 이동하여 계산하기 위한 list
dy = [0, 0, -1, 1]

def dfs(x, y):
  if x <= -1 or x >= N or y<= -1 or y>= M:
    return False

  if graph[x][y] == 1:
    graph[x][y] = 0

    for i in range(4):
      dfs(x + dx[i], y+dy[i])

    return True
  return False

answer = []
for _ in range(T):
  M, N, K = list(map(int, sys.stdin.readline().split()))

  graph = [[0]*M for _ in range(N)]

  for _ in range(K):
    x, y = map(int, input().split())
    graph[y][x] = 1

  cnt = 0
  for i in range(N):
    for j in range(M):
      if dfs(i, j):
        cnt +=1

  print(cnt)

# 입력을 먼저 싹 다 받고나서 dfs를 실행해야 출력할 때 안 꼬일 것이라 생각했는데
# 답을 보니 입력받을때부터 dfs를 돌리고 출력까지 한 다음에 다음 턴 테스트 케이스를 입력받았다
# graph_list = [0]*T
# for i in range(T) :
#     cnt = 0
#     graph = graph_list[i]
#     for j in range(N):
#         for k in range(M):
#             if graph[j][k] == 1:
#                 dfs(j, k)
#                 cnt += 1
#     print(cnt)




