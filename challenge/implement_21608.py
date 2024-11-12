# 1. 상하좌우만 가능
# 2. 좋아하는 학생이 자리에 앉았는지 확인
# 3. 앉았다면 -> 빈 칸중 학생과 가장 인접한 칸으로
# 4. 없다면 -> 여백이 가장 많은 칸으로
# 5. 행의 번호가 가장 작은 칸으로
# 6. 열의 번호가 가장 작은 칸으로
# 7. 칸의 후보를 담을 리스트가 있어야 할 듯?
# 8. 조건문에 따라 탈출시키기,,
# 9. 맨 마지막에 만족도 구하기
# Answer.
# 답 참고하면서 똑같이 작성했다고 생각했는데 왜 인덱스 오류가 나는가?
n = int(input())
data = [[0] * n for _ in range(n)]
students = [list(map(int, input().split())) for _ in range(n ** 2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for student in students:
    available = []

    for i in range(n):
        for j in range(n):
            # 빈자리가 있다면
            if data[i][j] == 0:
                prefer, empty = 0, 0

                # 동서남북 방향 확인하여
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    # 범위내에 있을 때
                    if 0 <= nx < n and 0 <= ny < n:
                        # 좋아하는 학생이 주위에 있다면 더해준다.
                        if data[nx][ny] in student[1:]:
                            prefer += 1

                        # 빈자리가 있다면 더해준다.
                        if data[nx][ny] == 0:
                            empty += 1

                available.append((i, j, prefer, empty))
    # 정렬
    available.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    data[available[0][0]][available[0][1]] = student[0]

answer = 0
score = [0, 1, 10, 100, 1000]
students.sort()

for i in range(n):
    for j in range(n):
        count = 0

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] in students[data[i][j] - 1]:
                    count += 1

        answer += score[count]

print(answer)

# N = int(input())
# stu = []
# for _ in range(N) :
#     stu.append(list(map(int, input().split())))
# position = [[0]*N for _ in range(N)] # 학생 배치도
# select = []                          # 학생 개인당 자리 후보군
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for i in range(N) :
#     now_stu = stu[i][0]
#     for j in range(N) :
#         for k in range(N) :
#             if position[j][k] == 0 : # 빈 자리여야 앉힐 수 있으므로, 빈 자리일 때 후보군에 들어감
#                 prefer = 0           # 후보군 선호도 디폴트 값
#                 blank = 0            # 후보군 빈자리 디폴트 값
#                 for l in range(4) :  # 해당 자리에 대하여 주변의 자리에, 선호도와 빈칸이 커야 좋은 자리가 되므로
#                     x = j + dx[l]    # 주변 자리에 대해서 탐색함
#                     y = k + dy[l]
#                     if 0 <= x < N and 0 <= y < N :
#                         if position[x][y] in stu[i][1:] : # 좋아하는 사람 목록에 있으면
#                             prefer += 1                   # prefer 증가
#                         if position[x][y] == 0 :          # 빈칸이라면
#                             blank += 1                    # blank 증가
#                 select.append((j,k,prefer,blank))             # 한 자리에 대한 주변 탐색(상하좌우)이 끝나면 후보군에 삽입
#
#     # 조건 우선순위별로 정렬
#     # 변수앞에 -가 붙으면 reverse. 즉, 큰 순서대로 정렬
#     # 변수뒤에 인덱스가 붙으면 변수를 넣어준 순서를 지정하는 것.
#     # 즉 -x[2]는 perfer을 큰 순서대로 정렬함
#     select.sort(key=lambda x: (-x[2], -x[1], x[0], x[1]))
#
#     # 정렬해서 제일 처음에 있는게 가장 좋은 자리이므로, 학생에게 자리 배정
#     position[select[0][0]][select[0][1]] = now_stu
#
# stu.sort()
# result = 0
# for j in range(N) :
#     for k in range(N) :
#         like_stu = 0
#         for l in range(4) :
#             x = j + dx[l]
#             y = k + dy[l]
#             if 0 <= x < N and 0 <= y < N :
#                 if position[x][y] in stu[position[j][k]-1][1:] :
#                     like_stu += 1
#         if like_stu == 0 :
#             result += 0
#         elif like_stu == 1 :
#             result += 1
#         elif like_stu == 2 :
#             result += 10
#         elif like_stu == 3 :
#             result += 100
#         elif like_stu == 4 :
#             result += 1000
# print(result)
#
#


