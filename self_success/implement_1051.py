# 항상 인덱스가 탈출하지 않도록 조건 검사를 넣어주자.. 귀찮더라도,.. ㅠㅠ

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

side = 0
for k in range(n) :
    for i in range(n) :
        for j in range(m) :
            if ( i+k < n  ) and ( j+k < m ) and ( graph[i][j] == graph[i][j+k] == graph[i+k][j] == graph[i+k][j+k] ) :
                side = k+1
print(side*side)