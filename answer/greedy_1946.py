# Answer
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank_asc = sorted(rank)
    top = 0
    result = 1

    # sorted한 덕에 서류성적 값은 좋은 순으로 왼쪽부터 정렬돼있음
    # 따라서 [][1] 값이 좋아지지 않는 한 top이 바뀔 수가 없음
    for i in range(1, len(rank_asc)) : # 0을 default로 초기값으로 해뒀으니 idx=1부터 비교
        if rank_asc[i][1] < rank_asc[top][1] : #sort로 이미 [][0] 값은 비교가 된 것이므로 비교를 한 케이스로 줄여버림
            top = i # 만약 두번째가 순위 값이 작다면 (순위는 낮은 수일수록 좋음) top 값이 바뀜
            result += 1
    print(result)


# from collections import deque
# T = int(input())
#
# for _ in range(T) :
#     score = []
#     N = int(input())
#     for _ in range(N) :
#         S_score, M_score = map(int, input().split())
#         score.append((S_score,M_score))
#     score_sort = deque(sorted(score))
#     score_sort.reverse()
#     print(score)
#     cnt = N
#
#     for i in range(len(score_sort)-1) :
#         if score_sort[i][0] > score_sort[i+1][0] and score_sort[i][1] < score_sort[i+1][0] :
#             score_sort.popleft()
#             cnt -= 1
#     print(cnt)
#     # for i in range(len(score)) :
#     #     if score[i][0] == score[i+1][0] :
#     #         score[i][1] < score[i+1][1] :