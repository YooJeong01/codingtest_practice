# 1. 큐에 입력을받고
# 2. pop을 한 걸 더하는데 그게 l보다 커지기 전까지만 pop을 함
# 3. 다리길이 +1 한게 하나를 건너는 시간



# Answer
import sys
input=sys.stdin.readline

# n : 트럭 수
# w : 다리 길이
# L : 다리 최대 하중
n, w, L = map(int, input().split())
truck = list(map(int, input().split()))

bridge = [0] * w
time = 0
# bridge에 모든 트럭이 지나갈 때 까지 반복
while bridge:
    time += 1
    bridge.pop(0)
    if truck:
        if sum(bridge) + truck[0] <= L:
            bridge.append(truck.pop(0))
        else:
            bridge.append(0)
print(time)


# n, w, L = map(int, input().split())
# right_q = list(map(int, input().split()))
# left_q=[]
# weight = 0
# cnt = 0
#
# while right_q :
#
#     while right_q :
#         if sum(left_q) + right_q[0] <= L :
#             left_q.append(right_q.pop(0))
#     cnt += 1 # 트럭 수 상관없이 한 번 지나간 흐름을 카운트
#
# t = cnt * (w+1)
# print(t)



