# Q. 방울미술
# 마술사가 3개의 컵을 탁자 위에 일렬로 세워 놓았다.
# 마술사는 3개의 컵 중 하나에 방울을 넣고, 이를 보여 준 뒤, 모든 컵을 엎었다.
# 마술사는 컵을 1회 이상 섞었다.
# 컵을 ‘한 번 섞는다’는 것은 인접한 두 컵 (왼쪽 컵-가운데 컵, 가운데 컵-오른쪽 컵)을 교환한다는 것을 의미한다.
# 마술사는 컵을 섞을 때마다 동전을 던져 앞면이 나오면 왼쪽 컵과 가운데 컵의 순서를 바꿨고,
# 뒷면이 나오면 오른쪽 컵과 가운데 컵의 순서를 바꿨다. 동전의 각 면이 나올 확률은 ½이었다.
# 마술사가 방울이 들어 있는 컵을 다른 컵과 교환할 때마다 방울이 한 번씩 울렸다.
# 당신은 마술사가 컵을 섞는 것을 잘 관찰하여 방울이 정확히 K번 울렸다는 것을 알고 있다.
# 이러한 사실을 알고 있는 상황에서, 현재 방울이 있을 확률이 가장 높은 컵의 위치를 구하는 프로그램을 작성하라.
#
# Input.
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 한 개의 줄로 이루어진다.
# 각 줄에는 문자열 S와 정수 K(0≤K≤1,000)가 공백 하나를 사이로 두고 주어진다.
# S는 컵을 섞기 전 방울이 있는 컵의 위치를 나타내며, 방울이 맨 왼쪽 컵에 있었다면 “o..”,
# 가운데 컵에 있었다면 “.o.”, 맨 오른쪽 컵에 있었다면 “..o”이다.
#
# Output.
# 각 테스트 케이스마다, 현재 방울이 있을 확률이 가장 높은 컵의 위치
# (단, 그러한 컵이 여러 개 있다면 그 중 가장 왼쪽 위치)를 구한 뒤,
# 맨 왼쪽이라면 0,
# 가운데라면 1,
# 맨 오른쪽이라면 2
# ...를 한 줄에 하나씩 출력한다.

# 방울이 컵을 섞을때마다 항상 울려야 하므로,, 가장자리로 이동하고나서는 반드시 가운데로도 와야 함


TC = int(input())
for t in range(TC) :
    ball = 0
    S, K = input().split()
    for i in range(len(S)) :
        if S[i] == 'o' :
            ball = i
    K = int(K)
    for j in range(K) :
        ball = ball - 1
        if ball < 0 :
            ball = 1
        elif ball >= 3 :
            ball = 1

    print(f"#{t+1} {ball}")