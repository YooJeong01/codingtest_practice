# 가장 자리인걸 어떻게 알수있나?
# -> 풀이)
# 공기(0)를 탐색하다가 치즈(1)를 만나면 그때마다 녹일 치즈 리스트에 추가함(한 번 돌때마다 0 주위만 탐색하기때문에
# 내부에 있는 치즈까지는 도달할수 없음. 즉, 가장자리만 녹일 치즈 리스트에 추가 되는 것!)
#
from collections import deque
n, m = map(int,input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
melt = []
cnt = 0
for i in range(n) :
    graph.append(list(map(int, input().split())))
    # 치즈는 1 공기는 0이라서 그냥 모든 원소를 합해도 치즈의 갯수만 늘어난다
    cnt += sum(graph[i])

def bfs() :
    # 0,0에서부터 시작
    q=deque([(0,0)]) # 괄호 주의!! deque(리스트[튜플()])
    melt = deque([])
    while q:
        x, y = q.popleft() # 계속 해야하기 때문에 popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and not visited[nx][ny]: # 범위탐색, 방문하지 않은 공기 영역 탐색
                visited[nx][ny] = 1 # 방문표시 바꾸기
                if graph[nx][ny] == 0 : # 공기인 경우
                    q.append((nx,ny))  # 이어서 탐색할수있게 해당 좌표를 큐에 추가
                elif graph[nx][ny] == 1 : # 치즈인 경우
                    melt.append((nx,ny)) # 공기가 아니라 큐에는 안들어가지만, 녹일 리스트에 추가
    for x, y in melt : # 치즈 녹이기 1 -> 0
        graph[x][y] = 0

    return len(melt) # 녹인 치즈 갯수를 리턴

t = 1
while True :
    visited = [[0] * m for _ in range(n)] # 매번 방문할때마다 초기화해줌 (근데 왜지?)
    melt_cnt = bfs() # 녹이는 갯수 리턴한 값 받아오기
    cnt = cnt - melt_cnt # 남은 치즈 개수
    if cnt == 0 :
        print(t)
        print(melt_cnt) # 직전에 남은 치즈 갯수 = 직전에 녹인 치즈 개수
        break
    t += 1


