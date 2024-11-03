# 1. 두개를 골랐을 떄 최대의 합이 나오는 조합을 최선의 선택으로
# 2. 그 합에 그 다음 최선의 선택 더하기
# 3. 마지막 값 더하기

# Answer.
import heapq
import sys

input = sys.stdin.readline

n = int(input())
card = []
for _ in range(n) :
    num = int(input())
    heapq.heappush(card,num)
    # 우선순위 큐는 들어간 순서 상관없이 높은 우선순위를 가진 원소를 먼저 처리하게 됨
    # 즉, 정렬되는것, 파이썬은 최소힙이라 가장 작은것부터 정렬됨

result = 0
while len(card)>1 :
    n1 = heapq.heappop(card) # 우서순위 큐에 따라 가장 작은 원소를 제거함
    n2 = heapq.heappop(card)
    result += n1 + n2 # pop해서 result에 각 원소를 더해줌
    heapq.heappush(card, n1+n2) # 둘의 합을 card 원소로 다시 넣어줌으로써 그 다음 원소와 계산될 때 자연스럽게 중복 계산 됨
print(result)

# N = int(input())
# num = []
# for _ in range(N) :
#     num.append(int(input()))
# num.sort()
#
# result = 0
# i= 0
# for i in range(N-2) :
#     result += (num[i] + num[i+1])*2
#     i += 2
#     if i == N-1 :
#         result += num[i]
#         break

# print(result)

