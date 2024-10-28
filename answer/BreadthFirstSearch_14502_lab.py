# Q.
# 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다.
# 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
#
# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며,
# 직사각형은 1×1 크기의 정사각형으로 나누어져 있다.
# 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
#
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
#
# 예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
# 이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다.
# 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.
#
# 2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.
# 2 1 0 0 1 1 0
# 1 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 1 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
#
# 바이러스가 퍼진 뒤의 모습은 아래와 같아진다.
# 2 1 0 0 1 1 2
# 1 0 1 0 1 2 2
# 0 1 1 0 1 2 2
# 0 1 0 0 0 1 2
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
# 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다.
# 위의 지도에서 안전 영역의 크기는 27이다.
#
# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.
#
# Input.
# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
#
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다.
# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고,
# 10보다 작거나 같은 자연수이다.
#
# 빈 칸의 개수는 3개 이상이다.
#
# Output.
# 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.



# 한 행씩 상하좌우에 2가 바로 연속하는지 검사
# 연속하면 그 자리가 2로 바뀜
# 1은 0이 있는 자리에 넣는다
# 1만 3개 넣는 함수를 따로 만들어서 중첩 반복문으로 모든 경우의 수의 3개 자리에 넣고
# 그때마다 2를 채워서 안전구역 개수 확인
# 반복문을 돌리고 안전구역(0)이 최대가MAX 되는 값 찾기


from collections import deque
from itertools import combinations
import copy
n, m = map(int, input().split())
# 상하좌우로 움직이는 변수
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = []
virus_graph = []
safe_graph = []
answer = 0

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            safe_graph.append([i,j])
        if graph[i][j] == 2:
            virus_graph.append([i,j])


def bfs(tmp_graph):
    queue = deque(virus_graph) # 스택과 큐처럼 양방향에서 in/out을 가능하게 함
    #virus_graph = copy.deepcopy(graph) # 2중 리스트인 경우는 그냥 copy만 하면 주소가 복사되기때문에 deepcopy를 해야 내용이 복사됨

    while queue: #바이러스가 남아있는 동안
        x, y = queue.popleft() # 기존의 pop은 오른쪽에서 꺼냄
        for i in range(4) :     # 바이러스를 상하좌우로 전파하는 부분
            nx = x + dx[i]      # 전파가 될 x 좌표
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0 :  # 실제로 전파가 가능한 영역(0)인지 확인
                tmp_graph[nx][ny] = 2
                queue.append((nx,ny))       # 바이러스(2)가 전파된 영역도 큐에 저장

    global answer
    cnt = 0

    for i in range(n) :
        cnt += tmp_graph[i].count(0)       # 안전 구역의 개수 확인

    answer = max(answer, cnt)

# 시간 초과 됨
# def makeWall(cnt):
#     if cnt == 3: # 벽을 3개 다 세웠다면
#         bfs()   # 바이러스 전파 시작
#         return
#
#     for i in range(n) :
#         for j in range(m) :
#             if graph[i][j] == 0 : # 벽을 세울 수 있는 영역(0)인지 확인
#                 graph[i][j] = 1     # 벽 세우기
#                 makeWall(cnt+1)     # 두번째 벽 세우기 시작 (이 부분이 재귀 되면서 3번째까지 수행하게 됨)
#                 graph[i][j] = 0     # 다시 벽 허물기 (백 트래킹) -> 벽을 세우는 다른 경우의 수를 위해서

def makeWallCombinations():
    safe_zones_combinations = combinations(safe_graph, 3)
    for walls in safe_zones_combinations :
        a, b, c = walls[0], walls[1], walls[2]

        graph[a[0]][a[1]] = 1
        graph[b[0]][b[1]] = 1
        graph[c[0]][c[1]] = 1

        tmp_graph = [item[:] for item in graph]

        bfs(tmp_graph)

        graph[a[0]][a[1]] = 0
        graph[b[0]][b[1]] = 0
        graph[c[0]][c[1]] = 0

makeWallCombinations()
print(answer)
