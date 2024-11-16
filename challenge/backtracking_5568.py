import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
nums = [input().strip() for _ in range(n)]

tmp = []
visited = [0]*n
result = set()
def bt(cnt) :
    if cnt == k :
        result.add(''.join(tmp))
        return
    for i in range(n) :
        if visited[i] : continue

        visited[i] = 1
        tmp.append(nums[i])

        bt(cnt+1)

        visited[i] = 0
        tmp.pop()

bt(0)
print(result)
print(len(result))

