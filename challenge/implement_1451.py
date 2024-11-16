# 1. 직사각형을 어떻게 나눌것인가?
# 2. 나눌수있는 경우에 수에 대해서, 각 직사각형의 내부 값의 합을 저장하고
# 3. 곱했을떄 max가 되는 조합 찾기?

# 직사각형을 3등분할수있는 경우의 수 6가지를 각각 따로 만들어서 계산 해야함

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

total3 = 0
for j in range(m-1, 0, -1) :
    tmp1 = 0
    for k in range(n) :
        tmp1 += sum(square[k][j:])
    for k in range(1, n):
        tmp2 = 0
        tmp3 = 0
        for i in range(k) :
            tmp2 += sum(square[i][:j])
        for i in range(k, n) :
            tmp3 += sum(square[i][:j])
        total3 = max(total3, tmp1*tmp2*tmp3)

total4 = 0
for j in range(1, m) :
    tmp1 = 0
    for k in range(n) :
        tmp1 += sum(square[k][:j])
    for k in range(1, n) :
        tmp2 = 0
        tmp3 = 0
        for i in range(k) :
            tmp2 += sum(square[i][j:])
        for i in range(k, n) :
            tmp3 += sum(square[i][j:])
        total4 = max(total4, tmp1*tmp2*tmp3)

total5 = 0
for j in range(1, n):
    tmp1 = 0
    for k in range(j) :
        tmp1 += sum(square[k])
    tmp2 = 0
    tmp3 = 0
    for i in range(1, m) :
        tmp2 = 0
        tmp3 = 0
        for k in range(j, n) :
            tmp2 += sum(square[k][:i])
            tmp3 += sum(square[k][i:])
        total5 = max(total5, tmp1*tmp2*tmp3)

total6 = 0
for j in range(1, n) :
    for k in range(1, m) :
        tmp2 = 0
        tmp3 = 0
        for i in range(j) :
            tmp2 += sum(square[i][:k])
            tmp3 += sum(square[i][k:])
        tmp1 = 0
        for i in range(j, n) :
            tmp1 += sum(square[i])
        total6 = max(total6, tmp1*tmp2*tmp3)

print(max(total1, total2, total3, total4, total5, total6))