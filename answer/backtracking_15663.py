# lst = list(set(arr)) 로 풀었더니 출력이 초과되어 실패했음

import sys
input = sys.stdin.readline

def backtracking() :
    if len(arr) == m :
        print(" ".join(map(str,arr)))
        return
    isDuplicate = 0 # 똑같은 수가 중복되는 걸 방지하기 위해 append 한 수가 중복인지 아닌지 확인하는 변수
    for i in range(n) :
        if not visited[i] and isDuplicate != lst[i] : # 중복이 아니고, 아직 방문하지 않았다면
            visited[i] = True
            arr.append(lst[i])
            isDuplicate = lst[i]
            backtracking()

            # 백트래킹 후에는 원상복구해야 조건에 맞춘 모든 경우의 수를 탐색하게 됨
            visited[i] = False
            arr.pop()

n, m = map(int,input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [False] * n

arr = []

backtracking()