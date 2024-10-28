# Q.
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
#
# Input.
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
# 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
# Output.
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.

# 양방향 그래프이고, 주어진 표가 서로 연결된 짝을 입력으로 주기 때문에 이렇게 해야함
#     0 1 2 3 4
# 0
# 1       1 1 1
# 2     1     1
# 3     1     1
# 4     1 1 1

# from collections import deque
#
# N, M, V = map(int, input().split())
#
# graph = [[False] * (N + 1) for _ in range(N + 1)]
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a][b] = True
#     graph[b][a] = True
#
# visited1 = [False] * (N + 1)  # dfs의 방문기록
# visited2 = [False] * (N + 1)  # bfs의 방문기록
#
#
# def bfs(V):
#     q = deque([V])  # pop메서드의 시간복잡도가 낮은 덱 내장 메서드를 이용한다
#     visited2[V] = True  # 해당 V 값을 방문처리
#     while q:  # q가 빌때까지 돈다.
#         V = q.popleft()  # 큐에 있는 첫번째 값 꺼낸다.
#         print(V, end=" ")  # 해당 값 출력
#         for i in range(1, N + 1):  # 1부터 N까지 돈다
#             if not visited2[i] and graph[V][i]:  # 만약 해당 i값을 방문하지 않았고 V와 연결이 되어 있다면
#                 q.append(i)  # 그 i 값을 추가
#                 visited2[i] = True  # i 값을 방문처리
#
#
# def dfs(V):
#     visited1[V] = True  # 해당 V값 방문처리
#     print(V, end=" ")
#     for i in range(1, N + 1):
#         if not visited1[i] and graph[V][i]:  # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
#             dfs(i)  # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)
#
#
# dfs(V)
# print()
# bfs(V)















from collections import deque
# bfs 너비 우선 탐색에서 쓰기 위해서 import하기

N, M, V = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]
# 2차원 배열로 받고 미리 전부 false로 초기화 할 거임
# 인덱스 번호를 노드 번호로 바로 사용하기 위해 0이 아닌 1부터 시작해서 N+1로 끝남


# input으로 서로 연결된 짝을 한 줄씩 제시하기 때문에 그걸 좌표라고 생각하고 그 때 False를 1로 바꿔줌
for _ in range(M) :
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# 방문했는지 확인하기 위한(스택같은) 1차원 배열을 False로 미리 초기화해서 선언함
bfs_visited = [False]*(N+1)
dfs_visited = [False]*(N+1)

# 깊이 우선 탐색은 재귀이기 때문에 deque를 사용하지 않음
def dfs(V) :
    # 1. 방문 표시
    dfs_visited[V] = True
    # 2. 표시 후 출력
    print(V, end=" ")

    # 3. 모든 노드를 순회하면서
    # 4. 방문했는지 검사하고
    # 5. 만약 방문하지 않았는데 현재 출력된(v) 노드랑 이웃하다(==1)면
    # 6. 재귀 호출해서 해당 노드를 i -> V로 입장을 바꿔 깊게 탐색하게 함
    #재귀
    for i in range(1, N+1) :
        if not dfs_visited[i] and graph[V][i] == 1 :
            dfs(i)

# 너비 우선 탐색은 재귀를 사용하지 않기 때문에 deque를 써야함
def bfs(V) :
    # 1. 현재 노드를 큐로 지정하기
    q = deque([V])
    # 2. 현재 노드를 방문 표시하기
    bfs_visited[V] = True

    # 3. 큐에 아무것도 남지 않을때까지
    # 4. FIFO 선입선출로 제일 먼저 들어온 노드를 popleft() 꺼내기
    # 5. 꺼낸 노드를 출력하기
    # 6. 모든 노드에 대해서
    # 7. 만약 방문하지 않았는데(스택에 없는데), 현재 큐랑 이웃하는 노드라면
    # 8. 스택에 추가
    # 9. 방문 표시
    # 10. 모든 노드에 대해서 돌면서 현재 큐랑 이웃하는데 방문하지 않은게 있는지 확인
    # 11. for문 끝나면(=현재 큐에 대해 이웃하는 노드가 모두 방문 표시 됐다면)
    # 12. popleft로 꺼내지는 다음 노드가 큐가 됨
    # 13. 반복
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N+1) :
            if not bfs_visited[i] and graph[V][i] == 1 :
                q.append(i)
                bfs_visited[i] = True


dfs(V)
print()
bfs(V)

















