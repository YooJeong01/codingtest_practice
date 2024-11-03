# Answer.
N=int(input())

# i에 대한 연산 횟수를 리스트 값 (dp[i])으로 저장
dp = [0]*(N+1)

# 1에 대한 최소 연산 횟수는 0 이므로 2부터 시작
for i in range(2, N+1):

    # case1. 1을 빼는 연산 : 10이면 9인 경우에서 횟수 +1 된 것이므로
    dp[i] = dp[i-1]+1

    # case2. 2를 나누는 연산 : case1과 case2 결과를 비교해서 작은 값을 리스트 값으로 저장함
    if i%2 == 0 :
        dp[i]=min(dp[i], dp[i//2] +1)
        # dp[i//2] + 1
        # dp[4] 인 경우
        # dp[2] 의 횟수에 + 1 을 한 것과 같다! -> 나누기만 한 번 더 수행 됨

    # case3. 3을 나누는 연산 : case1, case2, case3 결과를 비교해서 작은 값을 저장함
    # 이미 위의 코드를 지나오면서 case1, case2의 횟수의 크기 비교는 됐음
    if i%3 == 0 :
        dp[i]=min(dp[i], dp[i//3]+1)
print(dp[N])



# N = int(input())
# cnt = 0
# while N > 1 :
#     # 소수인 경우에만 -1?
#     if N > 1 and ( N % 5 == 0 or N % 7 == 0 or N % 13 == 0):
#         N = N - 1
#         cnt += 1
#     if N % 3 == 0 :
#         N = N/3
#         cnt += 1
#     elif N % 2 == 0 :
#         N = N/2
#         cnt += 1
# print(cnt)