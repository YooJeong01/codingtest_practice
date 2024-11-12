# Answer.
N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1, 0, -1) :
    if arr[i-1] > arr[i] :
        for j in range(N-1, 0, -1) :
            if arr[i-1] > arr[j] :
                arr[i-1], arr[j] = arr[j], arr[i-1]
                arr = arr[:i] + sorted(arr[i:], reverse=True)
                print(*arr)
                exit()
print(-1)

# N = int(input())
# arr = [[0]*N for _ in range(N)]
#
# visited = [False]*N
# def backtracking(start) :
#     if len(arr) == N :
#         print(" ".join(str,arr))
#         arr = []
#     visited[start] = True
#     arr.append(start)
#     for j in range(1,N) :
#         if not visited[j] :
#             arr.append(i)
#             visited[j] = True
#             backtracking(i)
