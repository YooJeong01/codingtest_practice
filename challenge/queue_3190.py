# Q.
# 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데,
# 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과
# 부딪히면 게임이 끝난다.
#
# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다.
# 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고
# 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
#
# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
#
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
# 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
#
# Input.
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100)
# 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
#
# 다음 K개의 줄에는 사과의 위치가 주어지는데,
# 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다.
# 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
#
# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
#
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며.
# 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L')
# 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
# X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.
#
#
# Output.
# 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
k = int(input())
maps = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):  # 사과의 위치
    x, y = map(int, input().split())
    maps[x][y] = 2

info = {}
l = int(input())
for _ in range(l):  # 뱀의 방향변환정보 (초, 방향 L:왼쪽 D:오른쪽)
    sec, direct = input().split()
    info[int(sec)] = direct

time = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y = 1, 1
maps[y][x] = 1
d = 0
snakes = deque([(1, 1)])

while True:
    nx, ny = x + dx[d], y + dy[d]
    # 뱀의 몸통에 닿거나 벽에 부딪히는 경우 종료
    if nx <= 0 or ny <= 0 or nx > n or ny > n or (nx, ny) in snakes:
        break
    # 사과를 먹지 못하면 꼬리 없애기
    if maps[ny][nx] != 2:
        a, b = snakes.popleft() # 안없애면 몸통 길이가 늘어나는 것임
        maps[b][a] = 0
    x, y = nx, ny
    maps[y][x] = 1
    snakes.append((nx, ny)) #어쨌든 한 칸 전진하기 때문에 바뀐 좌표 append
    time += 1

    # 시간에 해당하는 방향전환 정보가 있을 경우
    if time in info.keys():
        if info[time] == "D":
            d = (d + 1) % 4
        else:
            nd = 3 if d == 0 else d - 1
            d = nd
print(time + 1)

# N = int(input())
# K = int(input())
#
# graph = []
# for i in range(K) :
#     graph.append(list(map(int, input().split())))
#
# L = int(input())
# direction = []
# for i in range(L) :
#     direction.append(list(input().split()))
#
# def check_direction(time) :
#     for i in range(len(direction)) :
#         if time == direction[i][0] :
#             if direction[i][1] == "D" :
#                 return 1
#             elif direction[i][1] == "L" :
#                 return -1
#     return 0
#
#     4
# 3       1
#     2
#
# def go_foward(x,y,body,current_turn, next_turn) :
#     turn = current_turn + next_turn
#     if 0 >= turn :
#         turn = 4
#     elif turn > 4 :
#         turn = 1
#
#     if turn == 1 :
#         y += 1
#     elif turn == 2 :
#         x += 1
#     elif turn == 3 :
#         y -= 1
#     elif turn == 4 :
#         x -= 1
#
#
#     return x,y,turn
#
# def eat_apple(x,y) :
#     for j in range(K) :
#         if graph[j][0] == x and graph[j][1] == y :
#             return 1
#     return 0
#
# flag = 1
# current_turn = 1
# x, y, t = 0, 0, 0
# body = 1
#
# while flag :
#     # 방향 전환이 되는 시간인지 확인
#     move_dir = check_direction(t)
#
#     # 방향 전환이 되는 시간이라면
#     if move_dir != 0 :
#         # 전진하는 함수  호출
#         go_foward(x,y,body,current_turn,move_dir)
#
#     if eat_apple(x,y) == 1 :
#         body += 1
#
#     if 부딪혔다면 flag = 0
