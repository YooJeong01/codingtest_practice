import sys
input = sys.stdin.readline
T = int(input())

for test_case in range(1,T+1) :
    cnt = 0
    a, b, n = map(int,input().split())

    while n >= max(a,b) :
        if a > b :
            b += a
            cnt += 1
        else :
            a += b
            cnt += 1
    print(cnt)