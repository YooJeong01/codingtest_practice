def dfs(start) :
    if len(arr) == m :
        print(' '.join(map(str,arr)))
        return
    for i in range(start, n) : # 노드 트리를 생각하면 점점 start가 땡겨지기 떄문에 이런식으로 전달하면 조합이 겹치지 않음
        # 만약 그냥 list 길이만큼만 했다면 매번 루트노드부터 다시 시작하게 됨
        arr.append(lst[i])
        dfs(i)
        arr.pop()

n, m = map(int, input().split())
arr = []
lst = list(map(int, input().split()))
lst.sort()

dfs(0)