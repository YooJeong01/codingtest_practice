# 17144 미세먼지 안녕!
# 모두 탐색해야하니까 dfs?
# 매초 확산되니까 초마다 위치에 값이 변하는 걸 확인해야 할듯
# 확산되고 -> 이동(공청바람)
# 상하좌우로 칸이 있는지 확인, 값 누적해주기(본인의1/5+) -> 본인은 확산된 칸수*양 만큼 줄어듬
# 공청기 위치 기준으로 위쪽은 반시계 방향으로
# 아래쪽은 시계 방향으로 값 회전
# 만약 그때 인덱스가 공청기랑 맞닿으면 -1이 됨

# ver2.
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def solve(r, c, t, maps):
    # 공기 청정기 좌표 저장
    fresher = []
    for i in range(r):
        if maps[i][0] == -1: fresher.append((i, 0))

    def difussion():
        # 확산
        nonlocal maps
        scores = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if maps[i][j] > 0:
                    temp = maps[i][j]
                    for dir in range(4):
                        x, y = i + dx[dir], j + dy[dir]
                        if not (0 <= x < r and 0 <= y < c): continue
                        if maps[x][y] == -1: continue
                        scores[x][y] += maps[i][j] // 5
                        temp -= maps[i][j] // 5
                    scores[i][j] += temp

        maps = scores.copy()
        for x, y in fresher:
            maps[x][y] = -1
        return

    def freshing():
        nonlocal maps
        # 위쪽 공기청정기 순환
        i, j = fresher[0]
        temp = 0
        while 0 <= j + 1 < c:
            # 여기서는 while문이 끝나기 전까지는 temp가 초기화 되지 않으므로
            # 처음 원소 제외하고는 전부 다음것과 한 칸씩 스위칭 됨
            temp, maps[i][j + 1] = maps[i][j + 1], temp
            j += 1
        while 0 <= i - 1 < r:
            temp, maps[i - 1][j] = maps[i - 1][j], temp
            i -= 1
        while 0 <= j - 1 < c:
            temp, maps[i][j - 1] = maps[i][j - 1], temp
            j -= 1
        while 0 <= i + 1 < r and maps[i + 1][j] != -1:
            temp, maps[i + 1][j] = maps[i + 1][j], temp
            i += 1
        # 아래 공기청정기 순환
        i, j = fresher[1]
        temp = 0
        while 0 <= j + 1 < c:
            temp, maps[i][j + 1] = maps[i][j + 1], temp
            j += 1
        while 0 <= i + 1 < r:
            temp, maps[i + 1][j] = maps[i + 1][j], temp
            i += 1
        while 0 <= j - 1 < c:
            temp, maps[i][j - 1] = maps[i][j - 1], temp
            j -= 1
        while 0 <= i - 1 < r and maps[i - 1][j] != -1:
            temp, maps[i - 1][j] = maps[i - 1][j], temp
            i -= 1

    def result():
        answer = 0
        for i in range(r):
            for j in range(c):
                if maps[i][j] > 0:
                    answer += maps[i][j]
        return answer

    for _ in range(t):
        difussion()
        freshing()
    return result()


r, c, t = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(r)]
print(solve(r, c, t, maps))



# # ver1.
# # 입력 받기
# r, c, t = map(int,input().split())
# dust = []
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
# robot = []
# for i in range(r) :
#     dust.append(list(map(int, input().split())))
#
# def dustSpread(dust) :
#     # 미세먼지 확산
#     for j in range(r) :
#         spread = 0
#         for k in range(c) :
#             if dust[j][k] > 0 :
#                 for i in range(4) :
#                     nx = j + dx[i]
#                     ny = k + dy[i]
#                     if 0 <= nx < c and 0 <= ny < r :
#                         if dust[nx][ny] != -1 :
#                             dust[nx][ny] += int(dust[j][k] / 5)
#                             spread += 1
#                     else :
#                         break
#                 dust[j][k] -= int(dust[j][k] / 5) * spread
#     return dust
#
#
# def robot_position(dust) :
#     # 공기청소기 행의 위치(y) 좌표값 찾기
#     robot_top = 0
#     robot_bottom = 0
#     for j in range(r) :
#         if dust[0][j] == -1 :
#             robot_top = j
#             robot_bottom = j+1
#             break
#     return robot_top, robot_bottom
#
#
# # 상하를 기준으로 상만 행을 모아서 한 줄로 만들고 rotate 시킨다음에 c-1개씩 분배하면?
# # 공청기 작동
# def clean1(dust, robot_top, robot_bottom) :
#     dust_move=[]
#     for j in range(r) :
#         for k in range(c) :
#             if j == robot_top or j == 0 or ( j <= robot_top and k==0 ) or ( j <= robot_top and k==c-1) :
#                 if dust[j][k] != -1 :
#                     dust_move[j].append(dust[j][k])
#             if j == robot_bottom or j == r-1 or ( j >= robot_bottom and k==0 ) or ( j >= robot_bottom and k==c-1) :
#                 if dust[j][k] != -1 :
#                     dust_move[j].append(dust[j][k])
#
#     for i in range(r) :
#         if i != 0 or i != r-1 :
#             dust_move[i].reverse()
#     return dust_move
#
# def clean2(dust_move, robot_top, robot_bottom) :
#     dust_top = []
#     dust_bottom = []
#     for j in range(r) :
#         if j <= robot_top :
#             for k in range(len(dust_move[j])) :
#                 dust_top.append(dust_move[j][k])
#         if j >= robot_bottom :
#             for k in range(len(dust_move[j])) :
#                 dust_bottom.append(dust_move[j][k])
#     return dust_top, dust_bottom
#
# def clean3(dust, dust_top, robot_top) :
#     nx, ny = 0, 0
#     for i in range(len(dust_top)) :
#         if ny >= r :
#             nx += 1
#             ny = 0
#         if nx == 0 :
#             dust[nx][ny] = dust_top[i]
#             ny += 1
#         if nx == robot_top :
#             dust[nx][ny] = dust_top[i]
#             ny += 1
#         elif 0 < nx < robot_top :
#             if ny == 0 or ny == r-1 :
#                 dust[nx][ny] = dust_top[i]
#             ny += 1
#     return dust
#
# def clean4(dust, dust_bottom, robot_bottom) :
#     nx, ny = dust_bottom, 0
#     for i in range(len(dust_bottom)) :
#         if ny >= r :
#             nx += 1
#             ny = 0
#         if nx == robot_bottom :
#             dust[nx][ny] = dust_bottom[i]
#             ny += 1
#         if nx == r-1 :
#             dust[nx][ny] = dust_bottom[i]
#             ny += 1
#         elif robot_bottom < nx < r-1 :
#             if ny == 0 or ny == r-1 :
#                 dust[nx][ny] = dust_bottom[i]
#             ny += 1
#     return dust
#
#
# for _ in range(t) :
#     robot_top, robot_bottom = robot_position(dust)
#     dust = dustSpread(dust)
#     dust_move = clean1(dust, robot_top, robot_bottom)
#     dust_top, dust_bottom = clean2(dust_move, robot_top, robot_bottom)
#     dust = clean3(dust, dust_top, robot_top)
#     dust = clean4(dust, dust_bottom, robot_bottom)
#
#
# sum = 0
# for j in range(r) :
#     for k in range(c) :
#         if dust[j][k] != -1 :
#             sum += dust[j][k]
# print(sum)


