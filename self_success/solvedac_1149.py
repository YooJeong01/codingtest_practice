# 색이 연속되면 안 됨
#
# dp[1][1]+dp[2][0] or dp[1][2]+dp[2][0] / dp[1][0]+dp[2][1] or dp[1][2]+dp[2][1] / dp[1][0]+dp[2][2] or dp[1][1]+dp[2][2]

n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

for j in range(1,n) :
        dp[j][0] += min(dp[j-1][1], dp[j-1][2])
        dp[j][1] += min(dp[j-1][0], dp[j-1][2])
        dp[j][2] += min(dp[j - 1][0], dp[j - 1][1])

print(min(dp[n-1]))
