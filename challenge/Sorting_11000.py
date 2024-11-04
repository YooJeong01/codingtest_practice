# Answer
import sys
import heapq
input = sys.stdin.readline

N = int(input())
time = []

for _ in range(N):
    time.append(list(map(int,input().split())))
time.sort()

heap = [time[0][1]] # 끝나는 시간을 리스트인 heap에 저장 (현재 원소가 1개)
for i in range(1,N):
    if heap[0] <= time[i][0]: # 첫 원소랑 다음 시작시간을 비교
        heapq.heappop(heap) # 이어서 가능하다면 기존에 들어있던 끝나는시간을 pop (제일 왼쪾이 pop 됨)
    heapq.heappush(heap,time[i][1]) # 끝나는 시간을 heap에 추가
    # if문을 거칠때만 pop이 되기 때문에 이어서 할 수없는 경우는 바로 추가가 되어서
    # 결과적으로 heap 들어있는 원소 개수만큼이 강의실 개수가 된다

print(len(heap))


# N = int(input())
# lecture = []
#
# for _ in range(N) :
#     s, t = map(int, input().split())
#     lecture.append((s,t))
#
# lecture.sort()
#
# # 1. 끝나는 시간이 다음 수업시간 시작 보다 같거나 작다면 강의실 카운트 X
#
#
# for i in range(N) :
#     for j in range(i+1, N-1) :
#         if lecture[i][1] <= lecture[j][0] :
#             lecture.append((lecture[i][0], lecture[j][1]))
#             lecture.remove(lecture[i])
#             lecture.remove(lecture[j])
#             print(lecture)
#
# print(len(lecture))
