import sys
input = sys.stdin.readline

def backtracking () :
    if len(array) == m:
        print(" ".join(map(str, array)))
        return
    for i in lst :
        if i not in array : # 중복되는 원소 방지
            array.append(i)
            backtracking()
            array.pop()


n, m = map(int,input().split())
lst = list(map(int, input().split()))
lst.sort() # 사전 순으로 출력하기 위해 입력받은 무작위 순서의 원소를 정렬함
array = []

backtracking()