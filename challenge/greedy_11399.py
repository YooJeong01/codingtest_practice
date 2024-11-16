# Answer
# 그냥 작은순으로 정렬해서 더하는거였다..
#사람의 수
N = int(input())

#인출에 걸리는 시간
P = list(map(int, input().split()))

#정렬
P.sort()
result = 0

for i in range(1, len(P)+1):
    result += sum(P[:i])

print(result)
# n = int(input())
# arr = list(map(int, input().split()))
#
# # 1. 순서를 정한다
# # 2. 순서에 따라 각 사람의 웨이팅 시간을 구한다
# # 3. 웨이팅 시간들만 따로더해서 min을 계산한다
#
# visited=[0]*n
# waiting_time = []
# result = []
# def waiting(total) :
#     if len(waiting_time) == n :
#         result.append(sum(waiting_time))
#     for i in range(n) :
#         if not visited[i] :
#             visited[i] = True
#             total += arr[i]
#             waiting_time.append(total)
#             waiting(total)
#             visited[i] = False
# waiting(0)
# print(min(result))