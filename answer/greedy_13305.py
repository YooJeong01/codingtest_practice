# 1. 가장 작은 도시에서 남은 거리만큼 풀로 충전하기
# 2. 가장 작은 도시가 아니라면, 그 다음 도시로 갈 기름만 충전하기

# Answer
N = int(input())
gap = list(map(int,input().split()))
price = list(map(int,input().split()))

min_price = price[0]
total = price[0] * gap[0]
for i in range(1, N-1) :
    if min_price > price[i] :
        min_price = price[i]
    total += min_price * gap[i] # min_price가 안바뀌는 동안에도 계속 거기까지 가는 거리에 해당하는 기름값을 누적함
    # min_price가 바뀌면 변수값이 바뀌므로 바뀐값의 오일 값이 측정되어 누적됨..

print(total)



