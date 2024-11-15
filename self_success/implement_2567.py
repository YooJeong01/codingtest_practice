import sys
input = sys.stdin.readline
paper = [[0]*101 for _ in range(101)]
# 100 이하라서, 100으로 하게 되면 백준에서 런타임에러가 남.

N = int(input())
for _ in range(N) :
    a, b = map(int, input().split())
    for j in range(a, a+10) :
        for k in range(b, b+10) :
            paper[j][k] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0
for j in range(101) :
    for k in range(101) :
        flag = 0
        if paper[j][k] == 1 :
            for l in range(4) :
                x = dx[l]+j
                y = dy[l]+k
                if paper[x][y] == 0 :
                    cnt += 1

print(cnt)