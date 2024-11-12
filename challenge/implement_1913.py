# Answer.
N = int(input())
tg = int(input())

# 숫자를 채울 배열 만들기
arr = [[0]*N for _ in range(N)]

directy = [1,0,-1,0]
directx = [0,1,0,-1]

# num: 시작값, i,j: 인덱스, dr: 방향
num = N*N
i,j = 0,0
dr = 0
# 지정 값 인덱스
rlty,rltx = 0,0

# num이 0이 되기 이전까지 while문 실행
while num > 0:
    arr[i][j] = num
    # 지정값에 해당하면 인덱스 저장
    if num==tg:
        rlty, rltx = i+1, j+1
    # 범위를 벗어나거나 0이 아니면 방향을 변경한다.
    if i + directy[dr] < 0 or i + directy[dr] >= N or j + directx[dr] < 0 or j + directx[dr] >= N or arr[i + directy[dr]][j + directx[dr]] != 0:
        dr = (dr + 1) % 4
    i += directy[dr]
    j += directx[dr]
    num -= 1

for i in arr:
    print(*i)

print(rlty, rltx)


# N = int(input())
# target = int(input())
# graph = [[0]*N for _ in range(N)]
#
# target_r, target_c = 0, 0
#
# i = N*N
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# r, c, dr = 0, 0, 0
# while i > 0 :
#     graph[r][c] = i
#     if target == graph[r][c] :
#         target_r = r
#         target_c = c
#     if r + dx[dr] < 0 or r + dx[dr] >= N or c + dy[dr] < 0 or c +dy[dr] >= N or graph[r + dx[dr]][c + dy[dr]] != 0 :
#         dr = (dr + 1) % 4 # 인덱스 넘는 것 방지
#     r += dy[dr]
#     c += dx[dr]
#     i -= 1
# for i in graph :
#     print(*i)
# print(target_r, target_c)



