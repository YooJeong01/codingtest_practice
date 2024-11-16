import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int,input().split())
m = int(input())
family = [[] for _ in range(n+1)]

for _ in range(m) :
    u, v = map(int,input().split())
    family[u].append(v)
    family[v].append(u)

visited = [False for _ in range(n+1)]

def dfs(x,cnt) :
    global flag
    visited[x] = True
    if x == b :
        flag = True
        print(cnt)
    for people in family[x] :
        if visited[people] == False :
            dfs(people, cnt+1)
flag = False
dfs(a,0)
if flag == False :
    print(-1)