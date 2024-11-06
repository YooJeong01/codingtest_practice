# 1. 앞에서 한 것처럼, 다음 계단을 밟을때 or 다다음을 밟을 떄 누가 더 max인지 골라서 더하기?
# 2. 근데 이제 조건으로 세 계단 연속이 안되게, 마지막을 반드시 밟게

# Answer.
import sys
input = sys.stdin.readline

n = int(input())

stairs = [0] * 301
for i in range(1, n+1) :
    stairs[i] = int(input())

dp = [0]*301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n+1) :
    # 3번째 계단부터 2계단을 연속으로 걸을때와, 1계단을 건너 뛴 것을 비교해서 최댓값을 갱신함
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

print(dp[n])

# N = int(input())
#
# step =[]
# for _ in range(N) :
#     step.append(map(int, input().split()))
#
# total = step[0]
# cnt = 0
#
# for i in range(2,N-1) :
#     if step[i] > step[i-1] :
#         cnt = 0
#         total += step[i]
#     elif step[i] < step[i-1] and cnt < 1:
#         cnt += 1
#         total += step[i-1]
# total += step[N-1]
# print(total)

