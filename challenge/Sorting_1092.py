# Answer.
import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)
t = 0

if box[0] > crane[0] : t = -1
else :
    while box : # 박스가 남아있는동안
        for c in crane :
            if box and c < box[-1] : # 만약 가장 가벼운 상자를 들지 못한다면 그 다음 크레인으로 넘어감
                continue
            for b in box :
                if c >= b :
                    box.remove(b)
                    break # 크레인 한 대 당 하나의 박스만 이동시키므로 for b in box 탈출
        t += 1 # 크레인에게 모두 할당하고 나면 1분 지나있음


print(t)

# n = int(input()) # 크레인 수
# crane = list(map(int, input().split()))
# m = int(input()) # 박스 수
# box_weight = list(map(int, input().split()))
#
# crane.sort()
# box_weight.sort()
#
# move = [0]*(n+1)
#
# # 1. 크레인 제한 무게보다 상자 무게가 큰지 비교해야함
# # 2. 크레인 제한 무게중 제일 큰수가 상자무게의 제일 큰수보다 같거나 크면 다 옮길수 있다
# #
# # 1 2 3 총 몇번 크레인에 할당되는지 구하면 될듯?
# # 1 2 2
#
# while box_weight :
#     for j in range(m-1, 0, -1) :
#         for k in range(n-1, 0, -1) :
#             if crane[k] >= box_weight[j] :
#                 move[k] += 1
#                 box_weight.pop()
#
# print(max(move))



