# 14891번 톱니바퀴
# 정렬 문제 같음
# 1-0 / 0-1 인 경우 하나라도 움직이면 같이 딸려감
# 1-1 / 0-0 인 경우 안 딸려감. 정지 상태
# state[@][2] [@][6] 번째가 항상 맞닿는 위치가 됨
# 반시계 방향(-1) -> 왼쪽으로 한 칸씩 이동
# 시계 방향(+1) -> 오른쪽으로 한 칸씩 이동

# ver 2.
# 바퀴가 돌 때는 연쇄적으로 반응이 나타난다
# 아마 첫 코드가 틀린 이유도 연쇄적으로 동시다발적으로 돈다는 개념이 들어간 코드가 아니라서 그런듯?
# -> 이걸하려면 ver2처럼 재귀를 해야할듯!

from collections import deque
def right(idx, d): # 오른쪽 톱니바퀴 확인
    # 마지막 톱니는 확인 안함
    if idx > 3: # 인자로 어짜피 idx+1을 계속 받으므로 작아지는 경우는 없음
        return


    # 같은 극이 아니면 회전
    # 연쇄로 돌기 때문에 지금 톱니바퀴에서
    # idx-1(: 호출전에 메인이던 톱니바퀴의 번호)와 오른쪽에 이웃하는 톱니(idx)의 극이 다른지 확인
    if sawtooth[idx - 1][2] != sawtooth[idx][6]:
        # 본인이 돌고나면 나의 오른쪽 바퀴도 연쇄적으로 일어나므로 right()다시 호출
        # 방향은 본인 방향(d)의 반대로 돌기 때문에 -d로 인자 전달
        right(idx + 1, -d)
        # 본인은 돌기
        sawtooth[idx].rotate(d)


def left(idx, d):
    # 첫번째 톱니는 확인하지 않음
    if idx < 0: # 인자로 어짜피 idx-1을 계속 받으므로 커지는 경우는 없음
        return


    # 같은 극이 아니면 회전
    # 연쇄로 돌기 때문에 지금 톱니바퀴에서
    # idx+1(: 호출전에 메인이던 톱니바퀴의 번호)와 왼쪽에 이웃하는 톱니(idx)의 극이 다른지 확인
    if sawtooth[idx][2] != sawtooth[idx + 1][6]:
        # 본인이 돌고나면 나의 오른쪽 바퀴도 연쇄적으로 일어나므로 left()다시 호출
        # 방향은 본인 방향(d)의 반대로 돌기 때문에 -d로 인자 전달
        left(idx - 1, -d)
        # 본인은 돌기
        sawtooth[idx].rotate(d)


# 톱니바퀴 4개 입력받기
sawtooth = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())   # 회전 횟수

for _ in range(k):
    # 회전 정보(회전 톱니 번호 인덱스, 회전 방향) 입력받기
    idx, d = map(int, input().split())
    idx -= 1 # 톱니바퀴 번호가 1~4 라서 -1을 해줘야 인덱스 번호가 됨


    # 회전할 톱니 번호의 시계방향, 반시계방향이 회전 가능한지 확인하고 회전한다
    # -d인 이유는 회전할 톱니번호가 회전하는 방향의 반대방향으로 회전해야 하기 때문
    left(idx - 1, -d)   # 현재 톱니바퀴(idx)를 기준으로 왼쪽은 idx-1이 되고, 방향(d)이 반대로 돈다(-d)
    right(idx + 1, -d)  # 현재 톱니바퀴(idx)를 기준으로 오른쪽은 idx+1이 되고, 방향(d)이 반대로 돈다(-d)

    # 회전할 톱니 번호의 톱니도 회전. 이웃하는 바퀴들은 돌렸기 때문에 본인은 미리 돌려도 됨
    sawtooth[idx].rotate(d)


# 점수 계산하여 출력
score = 0
for i in range(4):
    if sawtooth[i][0] == 1:
        score += 2 ** i

print(score)


# ver 1.
# # 톱니바퀴 상태를 담은 리스트
# state = []
# for i in range(4) :
#     state.append(list(map(int,input())))
# # 회전 횟수
# turn = int(input())
# # 회전한 톱니바퀴 번호와 그 방향
# move = []
# for i in range(turn) :
#     move.append(list(map(int,input().split())))
#
# print("original list : ")
# for i in range(4) :
#     print(state[i])
#
# def arr_move_left(x, arr) :
#     temp = arr[x][0]
#     for j in range(0, 7):
#         temp = arr[x][j]
#         arr[x][j] = arr[x][j + 1]
#     arr[x][7] = temp
#     return arr
#
# def arr_move_right(x, arr) :
#     temp = arr[x][7]
#     for j in range(7, 0, -1):
#         arr[which][j] = arr[x][j - 1]
#     arr[x][0] = temp
#     return arr
#
#
# for i in range(turn):
#     # 누가 중심으로 도는지 먼저 확인
#     which = move[i][0]-1
#     # 방향에 따라 바뀜
#     if move[i][1] == 1 : # 본인은 먼저 바꿈
#         arr_move_right(which,state)
#         print("시게 방향 회전")
#         for k in range(4):
#             print(state[k])
#         # for j in range(0,7):
#         #     temp = state[which][j]
#         #     state[which][j] = state[which][j+1]
#         # state[which][7] = temp
#         if which == 0 : # 1,4번째 가장 사이드 톱니 바퀴인 경우
#             if state[which][2] != state[which + 1][6] :
#                 arr_move_left(which+1,state)
#         if which == 3 :
#             if state[which][6] != state[which - 1][2] :
#                 arr_move_left(which-1,state)
#         else : # 2,3번째 톱니 바퀴인 경우
#             if state[which][6] != state[which - 1][2] :
#                 arr_move_left(which-1,state)
#             if state[which][2] != state[which + 1][6] :
#                 arr_move_left(which+1,state)
#
#     if move[i][1] == -1 :
#         arr_move_left(which,state)
#         print("반시계 방향 회전")
#         for k in range(4):
#             print(state[k])
#         if which == 0 : # 1,4번째 가장 사이드 톱니 바퀴인 경우
#             if state[which][2] != state[which + 1][6] :
#                 arr_move_right(which+1,state)
#         if which == 3 :
#             if state[which][6] != state[which - 1][2] :
#                 arr_move_right(which-1,state)
#         else : # 2,3번째 톱니 바퀴인 경우
#             if state[which][6] != state[which - 1][2] :
#                 arr_move_right(which-1,state)
#             if state[which][2] != state[which + 1][6] :
#                 arr_move_right(which+1,state)
#
# print("result list : ")
# for i in range(4) :
#     print(state[i])
