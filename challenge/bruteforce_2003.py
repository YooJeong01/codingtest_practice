# Answer
# 그냥 이중 for문을 하면 시간초과가 나옴
# 이중 포인터 문제임..
N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

total = arr[0]
start = 0
end = 1

while end <= N and start <= end:
    if total == M:
        result += 1
        total -= arr[start]
        start += 1

    elif total < M:
        if end == N:
            break
        total += arr[end]
        end += 1
    else:
        total -= arr[start]
        start += 1


print(result)

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
#
# cnt = 0
# for i in range(n) :
#     total = 0
#     if i > n : continue
#     for j in range(i,n) :
#         total += arr[j]
#         if total == m :
#             cnt += 1
#             break
# print(cnt)