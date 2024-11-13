# Answer.
N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]

across_digit = {
    0 : 5,
    1 : 3,
    2 : 4,
    3 : 1,
    4 : 2,
    5 : 0
}

def cal_total(num) :
    result = 0
    for i in range(N) :
        for j in range(6) :
            if dice[i][j] == num :
                across_num = dice[i][across_digit[j]] # 두번째 주사위의 윗면의 값은 이전에 저장해놓은 수의 면 번호가 된다
                if 6 in [num, across_num] : # 만약 윗/아랫면에 6이 포함되어있다면
                    result += 4 if 5 in [num, across_num] else 5 # 5도 포함돼있다면, 옆면의 최댓값은 4, 6만 포함이라면 최댓값은 5
                else : # 6이 포함되지 않았다면, 옆면의 최댓값은 6
                    result += 6
                num = across_num # 다시 윗면이 그 다음 주사위의 바닥면으로 감
                break
    return result

def solve() :
    result = 0
    for i in range(1,7) :
        result = max(result, cal_total(i))
        # cal_total(변수)
        # 변수 자리에 들어가는 건 맨 처음 아래에 놓일 주사위의 윗면의 값이 된다
    print(result)

solve()
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# cube = []
# for _ in range(N) :
#     cube.append(list(map(int,input().split())))
#     # 해당 숫자의 인덱스 번호를 찾고 그만큼 rotate하면 주사위 옆면이 맞게 될듯?
#
# stack = [[0]*6 for _ in range(N)]
# stack[0] = cube[0]
# for i in range(N-1) :
#     for j in range(6) :
#         if stack[i][0] == cube[i+1][j] :
#             cube[i + 1] = cube[i + 1][j:] + cube[i + 1][:j]
#     stack.append(cube[i+1])
# print(stack)
#
# total = 0
# cnt = 0
# result = []
# def calc(cnt, total) :
#     if cnt == N :
#         result.append(total)
#     for i in range(cnt, N) :
#         for j in range(6) :
#             total += stack[i][j]
#             calc(i+1, total)
#
# print(result)