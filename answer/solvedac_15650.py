n, m = map(int, input().split())
array = []

def backtracking(start) :
    if len(array) == m :
        print(" ".join(map(str, array)))
        return
    for i in range(start, n+1) :
        if i not in array :
            array.append(i)
            backtracking(i)
            array.pop()

backtracking(1)