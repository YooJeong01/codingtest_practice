# 경사로

# n*n
# l =  경사로의 가로 길이 (높이는 무조건 1)

n, l = map(int, input().split())
road = []
for i in range(n) :
    road.append(input())

# 경사로를 놓을 수 이쓴ㄴ 조건인지 검사 (@>=2)
# 가로로 한 번, 세로로 한 번 훑어야 할 듯
# 행을 반으로 잘라서 앞과 뒤에서 각각 검사해야하는가?
route = 0
cnt = 0
for j in range(0, n) :
    k = 0
    while road[j][k] == road[j][k+1] :
        cnt += 1
        k += 1
        if k >= n : break;
    if k < n and road[j][k]-road[j][k-1] <= 1 and cnt >= l :
        route += 1


