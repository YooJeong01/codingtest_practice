import sys
input = sys.stdin.readline

def backtracking(start):
    if len(array) == m:
        print(" ".join(map(str, array)))
        return

    for i in range(start, n+1): # 점점 숫자가 커져야 하기 때문에 start를 인자로 넘겨준다
        array.append(i) # 중복되도 상관없어서 not in array 하지 않아도 됨
        backtracking(i) # 현재 append 한 값을 추가해준다
        array.pop()

n, m = map(int,input().split())
array = []

backtracking(1)