# Answer : 둘러쌓여있는지를 확인한다
h, w= [*map(int, input().split())]
graph = [*map(int,input().split())]


total = 0
for i in range(1,w-1) :
    left_max = max(graph[:i])
    right_max = max(graph[i+1:])
    compare = min(left_max, right_max)
    if graph[i] < compare : # 둘러쌓여있다면
        total += compare - graph[i]

print(total)