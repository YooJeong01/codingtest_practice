# 1. 좌우 한칸에 대해서 차이 조사
# 2. 좌우 두번째 칸에 대해서, 한칸꺼보다 작다면 통과, 아니면 다시 크기 차이 비교

import sys
input = sys.stdin.readline

T = 10
for i in range(T) :
    n = int(input())
    home = list(map(int, input().split()))
    cnt = 0
    diff = []
    for j in range(2,n-2) :
        r_diff, l_diff = 0, 0
        if home[j] > home[j+1] and home[j] > home[j+2] :
            r_diff = home[j]-home[j+1]
            if home[j+1] < home[j+2] :
                r_diff = home[j] - home[j+2]
        if home[j] > home[j-1] and home[j] > home[j-2] :
            l_diff = home[j] - home[j-1]
            if home[j-1] < home[j-2] :
                l_diff = home[j] - home[j-2]
        diff.append(min(r_diff,l_diff))
    print(f"#{i+1} {sum(diff)}")

