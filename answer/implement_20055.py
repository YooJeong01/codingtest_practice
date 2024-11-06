# 1. 절반 지점이 내리는 위치
# 2. 내구도가 1 이상 있어야 이동 가능
# 3. 내구도가 9이라면


from sys import stdin
from collections import deque


def solution(N, K, A):
    answer = 0
    belt = deque([False] * N)

    while True:
        answer += 1

        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        A.rotate(1)
        belt.rotate(1)

        # 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
        belt[N - 1] = False

        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        for i in range(N - 2, -1, -1):
            # 2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
            if belt[i] and not belt[i + 1] and A[i + 1] > 0:
                belt[i], belt[i + 1] = False, True
                A[i + 1] -= 1

        # 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
        belt[N - 1] = False

        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        if A[0] > 0:
            belt[0] = True
            A[0] -= 1

        # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
        if A.count(0) >= K:
            break

    return answer


# input
N, K = map(int, stdin.readline().split())
A = deque(list(map(int, stdin.readline().split())))

# response
response = solution(N, K, A)
print(response)
