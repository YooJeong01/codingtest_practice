# 1. -(가장 큰수)에 가장 작은수를 더하면 가장 작은 값이 나오지 않을까?
# 2. 홀수는 숫자 짝수는 연산자 (괄호가 들어가기 전)

# Answer
import sys
S = sys.stdin.readline().strip().split('-')
temp = []

for i in S : # - 기준으로 잘린 리스트들
    cnt = 0
    for j in i.split('+') : # +를 기준으로 요소들을 더함
        cnt += int(j)

    temp.append(cnt) # 결과값 리스트에  추가

result = temp[0] # 맨 처음값 제외하고 전부 빼면 최소값 -> 왜냐면 나뉘는 기준이 - 였기 때문에 처음 이후로는 다 앞에 -가 붙어야함
for i in temp[1:] : # 두번째값부터 끝까지 result에서 빼준다
    result -= i

print(result)

# import sys
# input = sys.stdin.readline
#
# lis = input()
# lis2 = []
# for i in range(len(lis)) :
#     if lis[i] != '+' or lis[i] != '-' :
#         num += list[i]