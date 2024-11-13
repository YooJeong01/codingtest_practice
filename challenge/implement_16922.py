# 만들수있는 모든 조합을 리스트에 넣는데
# set으로 중복 거르고
# 갯수 카운트?
# Answer -> 백트래킹

n = int(input())
roma = [1, 5, 10, 50]
arr = [0] * 1001
num = 0


def dfs(depth, start):
    global num
    if depth == n:
        arr[num] = 1
        return

    for i in range(start, 4):
        num += roma[i]
        dfs(depth + 1, i)
        num -= roma[i]


dfs(0, 0)
print(sum(arr))