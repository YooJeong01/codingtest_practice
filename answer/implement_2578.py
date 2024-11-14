import sys
input = sys.stdin.readline
bingo = []
answer = []

for _ in range(5) :
    bingo.append(list(map(int, input().split())))

# for _ in range(5) :
#     answer.append(list(map(int, input().split())))
for i in range(5) :
    answer += list(map(int, input().split()))


def check(bingo) :
    check_num = 0

    for x in bingo :
        if x.count(0) == 5 :
            check_num += 1

    for y in range(5) :
        num = 0
        for z in range(5) :
            if bingo[z][y] == 0 :
                num += 1
        if num == 5 :
            check_num += 1

    num = 0
    for left in range(5) :
        if bingo[left][left] == 0 :
            num += 1
    if num == 5 :
        check_num += 1

    num = 0
    for right in range(5) :
        if bingo[right][4-right] == 0 :
            num += 1
    if num == 5 :
        check_num += 1

    return check_num

answer_cnt = 0
for i in range(25) :
    for j in range(5) :
        for k in range(5) :
            if answer[i] == bingo[j][k] :
                bingo[j][k] = 0
                answer_cnt += 1

    if answer_cnt >= 12 :
        if check(bingo) >= 3 :
            print(answer_cnt)
            break

# cnt = 0
# answer_cnt = 0
# for j in range(5) :
#     for k in range(5) :
#         answer_cnt += 1
#         for l in range(5) :
#             try :
#                 idx = bingo[l].index(answer[j][k])
#                 r = l
#                 c = idx
#             except :
#                 continue
#         bingo[r][c] = 0
#
#         if sum(bingo[r]) == 0 :
#             cnt += 1
#         if bingo[0][c] + bingo[1][c] + bingo[2][c] + bingo[3][c] + bingo[4][c] == 0 :
#             cnt += 1
#         if bingo[0][0] + bingo[1][1] + bingo[2][2] + bingo[3][3] + bingo[4][4] == 0 :
#             cnt += 1
#         if bingo[0][4] + bingo[1][3] + bingo[2][2] + bingo[3][1] + bingo[4][0] == 0 :
#             cnt += 1
#
#         if cnt >= 3 :
#             print(answer_cnt)
#             exit()



