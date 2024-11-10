# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5
#
# dp[0][0] = 7
# dp[0][0] + dp[1][0] = 10    | dp[0][0] + dp[1][1] = 15
# dp[1][0] + dp[2][0] = 18    | dp[1][0] + dp[2][1] = 11  | dp[1][1] + dp[2][2] = 15
#                             |           vs              |
#                             | dp[1][1] + dp[2][1] = 16  |
# dp[2][0] + dp[3][0] = 20    | dp[2][0] + dp[3][1] = 25  | dp[2][1] + dp[3][2] = 20  | dp[2][2] + dp[3][3] = 19
#                             |           vs              |           vs              |
#                             | dp[2][1] + dp[3][1] = 23  | dp[2][2] + dp[3][2] = 19  |
# ...
# 사이드 빼고는 항상 갈림길이 2개에서 오기 때문에 그 중 큰 것을 선택해야함 -> max(a,b)



import sys

n = int(sys.stdin.readline())
dp = []
for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0: # 제일 왼쪽인 경우
            dp[i][j] += dp[i - 1][j]
        elif j == i: # 제일 오른쪽인 경우
            dp[i][j] += dp[i - 1][j - 1]
        else:   # 가운데 갈림길인 경우
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[n - 1]))