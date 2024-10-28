# Q.
# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서,
# 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.
#
# 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다.
# 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다.
# 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다.
# (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)
#
# 예를 들어, 그림이 아래와 같은 경우에
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
#
# 적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1)
# 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)
#
# 그림이 입력으로 주어졌을 때,
# 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.
#
# Input.
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)
# 둘째 줄부터 N개 줄에는 그림이 주어진다.
#
# Output.
# 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를
# 공백으로 구분해 출력한다.

# 1. N과 graph 입력받기
# 2. bfs 구현?
# 3. dx, dy 해서 bfs 한 번 끝날때마다 구역 갯수가 카운트
# (X) 4. 이미 본 곳은 못가게 한 문자로 통일해두기 -> X? X가 아닐때만 탐색하도록
# 4. visited[][]를 활용해 방문한 노드 표시하기
# 5. 일반 구역 구하고 나면 적록색맹을 위해 G=R로 치환해서 구역 구하기

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y) :
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :
                if not visited[nx][ny] and graph[nx][ny] == graph[x][y] :
                    visited[nx][ny] = 1
                    q.append((nx, ny))

N = int(input())
graph = []
visited = [[0]*N for _ in range(N)]

for _ in range(N) :
    graph.append(list(input()))

cnt = 0
# 적록색약이 아닌 사람이 볼 때의 구역을 먼저 구하고
for j in range(N) :
    for k in range(N) :
        if visited[j][k] != 1 :
            bfs(j,k)
            cnt += 1

# 이제는 원본 그래프를 훼손해도 되므로 G를 R로 바꾸고
for j in range(N) :
    for k in range(N) :
        if graph[j][k] == 'G' :
            graph[j][k] = 'R'

visited = [[0]*N for _ in range(N)]

# 그래프에 B와 R만 있는 상태(적록색약)에서 구역의 갯수를 다시 구한다
cnt2 = 0
for j in range(N) :
    for k in range(N) :
        if not visited[j][k] :
            bfs(j,k)
            cnt2 += 1



print(cnt, cnt2)







