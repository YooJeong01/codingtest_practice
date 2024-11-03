# 항상 반만 맞추네,, 뭔가 그럴듯한데 어긋남,,

# 1. 시작 시간을 기준으로 정렬 -> 끝나는 시간을 기준으로 정렬해야 더 많은 회의가 가능함
# 2. 같은 시작 시간일때 더 짧은 것 선택
# 3. 그 다음 시작 시간은 이전 회의의 종료시간이 됨

# Answer
N = int(input())
conference = []
for _ in range(N) :
    a, b = map(int, input().split())
    conference.append((a,b))
conference.sort(key=lambda x : (x[1], x[0]))
# print(conference)

cnt = 1
end_time = conference[0][1]

for i in range(1,N) :
    if conference[i][0] >= end_time :
        end_time = conference[i][1]
        cnt += 1
print(cnt)

# while True :
#     for i in range(N) :
#      if conference[i][0] == conference[i+1][0] :
#
#          min(conference[i][1]-conference[i][0],conference[i+1][1]-conference[i+1][0])
#
#      start_time <= conference[j][0] :
#         # 시작 시간 전달
#      카운트 +1