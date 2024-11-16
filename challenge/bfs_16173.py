from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n) :
    graph.append(list(map(int, input().split())))

dx = [1,0]
dy = [0,1]

visited = [[False]*n for _ in range(n)]
def bfs(x,y) :
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q :
        x, y = q.popleft()
        if graph[x][y] == -1 : return "HaruHaru"
        for i in range(2) :
            nx = x + dx[i]*graph[x][y]
            ny = y + dy[i]*graph[x][y]
            if 0 <= nx < n and 0 <= ny < n :
                if not visited[nx][ny] :
                    visited[nx][ny] = True
                    q.append((nx,ny))
    return "Hing"

print(bfs(0,0))

