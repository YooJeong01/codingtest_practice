# 가로세로 가장 큰 길이 곱에서
# 가로세로 가장 작은 길이 곱을 빼면 면적
# 스택?
# 정렬해서 가장 크고 작은거 뽑아서 곱하기?

# 1,2 -> width
# 3,4 -> heigth

# 왜 내 코드는 정답이 안되는지 모르겠음....
# Answer.
# 동1 서2 남3 북4
s = []  # 방향, 거리 저장 리스트
x = []  # 가로 길이들 리스트
y = []  # 세로 길이들 리스트
lownum = []  # B의 가로 세로 길이

k = int(input())

for i in range(6):
    way, dist = map(int, input().split())  # 방향, 거리 입력
    s.append([way, dist])
    if s[i][0] == 3 or s[i][0] == 4:  # 세로 저장
        x.append(s[i][1])
    if s[i][0] == 1 or s[i][0] == 2:  # 가로 저장
        y.append(s[i][1])

# B의 길이 추출
for i in range(6):
    if s[i][0] == s[(i + 2) % 6][0]:
        lownum.append(s[(i + 1) % 6][1])

print(((max(x) * max(y)) - (lownum[0] * lownum[1])) * k)

# 방법 1
k = int(input())
max_w, max_h = 0, 0
min_w, min_h = 999, 999

for i in range(6) :
    side, length = map(int, input().split())
    if side == 3 or side == 4 :
        max_h = max(max_h, length)
        min_h = min(min_h, length)
    elif side == 1 or side == 2 :
        max_w = max(max_w, length)
        min_w = min(min_w, length)
cnt = ((max_h * max_w) - (min_h * min_w)) * k
print(cnt)

# 방법 2
k = int(input())
s = []
l = []
for i in range(6) :
    side , length = map(int, input().split())
    if side == 3 or side == 4 :
        s.append(length)
    if side == 1 or side == 2 :
        l.append(length)
cnt = ( max(s)*max(l) - min(s)*min(l) ) * k
print(cnt)
