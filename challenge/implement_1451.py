# 1. 직사각형을 어떻게 나눌것인가?
# 2. 나눌수있는 경우에 수에 대해서, 각 직사각형의 내부 값의 합을 저장하고
# 3. 곱했을떄 max가 되는 조합 찾기?

# 직사각형을 3등분할수있는 경우의 수 6가지를 각각 따로 만들어서 계산 해야함
#https://leeiopd.tistory.com/entry/BOJ-1451-%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95%EC%9C%BC%EB%A1%9C-%EB%82%98%EB%88%84%EA%B8%B0-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
square = [[0]*m for _ in range(n)]
for _ in range(n) :
    square.append(list(map(int,input())))



total1 = 0
for s in range(1, m-1) :
    for e in range(m-1, s, -1) :
        tmp1 = 0
        tmp2 = 0
        tmp3 = 0
        for k in range(n) :
            tmp1 += sum(square[k][:s])
            tmp2 += sum(square[k][s:e])
            tmp3 += sum(square[k][e:])
        total1 = max(total1, tmp1*tmp2*tmp3)

total2 = 0
for s in range(1, n-1):
    for e in range(n-1, s, -1) :
        tmp1 = 0
        for i in range(s) :
            tmp1 += sum(square[i])
        tmp2 = 0
        for i in range(s, e) :
            tmp2 += sum(square[i])
        tmp3 = 0
        for i in range(e, n) :
            tmp3 += sum(square[i])
        total2 = max(total2, tmp1*tmp2*tmp3)