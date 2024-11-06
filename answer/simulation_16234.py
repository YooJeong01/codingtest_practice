# 1. 이동이니까 dfs bfs
# 2. 인구 이동을 하게 되면 연합한 곳과 인구를 절반씩 나뉜다
# 3. 상하좌우로 인구 차이가 L <= @ <= R 을 만족하는 동안은 인구 이동이 계속된다
# 바이러스 전파 느낌?
from collections import deque

# N : 맵 크기 / L <= <= R : 인구 이동 조건
N, L, R = map(int, input().split())

graph = []
for _ in range (N) :
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 얘가 한 번 호출될때마다 연합이 하나 생성된다
def bfs(x,y) :
    q = deque()
    q.append((x,y))
    union = []
    union.append((x,y))
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or ny >= N or nx <= 0 or ny <= 0 or visited[nx][ny] == 1 :
                continue
            if L <= abs(graph[nx][ny] - graph[x][y]) <= R :
                visited[nx][ny] = True
                q.append((nx,ny))
                union.append((nx,ny))

    return union

day = 0
# 소요된 날 계산
while True:
    flag = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0: # 아직 방문을 안했다면
                visited[i][j] = 1
                country =  bfs(i,j) # 방문하여 이웃 노드들간의 인구 이동 시작

                if len(country) > 1 : # 연합이 생성됐다면
                    flag = 1
                    # 인구 분배
                    people = sum(graph[x][y] for x, y in country) // len(country)
                    for x, y in country:
                        graph[x][y] = people
    # 더이상 인구 이동이 일어나지 않는 경우
    if flag==0:
        print(day)
        break # 여기서 while문 탈출함

    day += 1








