# Q.
# 각각 부피가 A, B, C(1≤A, B, C≤200) 리터인 세 개의 물통이 있다.
# 처음에는 앞의 두 물통은 비어 있고, 세 번째 물통은 가득(C 리터) 차 있다.
# 이제 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있는데,
# 이때에는 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다.
# 이 과정에서 손실되는 물은 없다고 가정한다.
#
# 이와 같은 과정을 거치다보면 세 번째 물통(용량이 C인)에 담겨있는 물의 양이 변할 수도 있다.
# 첫 번째 물통(용량이 A인)이 비어 있을 때, 세 번째 물통(용량이 C인)에
# 담겨있을 수 있는 물의 양을 모두 구해내는 프로그램을 작성하시오.
#
# Input.
# 첫째 줄에 세 정수 A, B, C가 주어진다.
#
# Output.
# 첫째 줄에 공백으로 구분하여 답을 출력한다. 각 용량은 오름차순으로 정렬한다.

# A(8mL) B(9mL) C(10mL)
# 존재하는 물의 양 = C (10mL)
# C -> A, B
# while 문 end 조건 => A가 0mL가 될 때(처음 제외)
# 두개만 골라서 C를 나누는 경우의 수??

a, b, c = map(int, input().split())
ans = []

from collections import deque

q = deque()
q.append([0, 0, c])
check = [[0] * 201 for i in range(201)]
ans = [0 for i in range(201)]


def bfs():
    while q:
        x, y, z = q.popleft()

        if check[x][y] == 1:  # 이미 했었던 조합이면 pass
            continue

        check[x][y] = 1  # flag용도

        if x == 0:  # 문제에서 요구한 조건
            ans[z] = 1

        # A->B
        if x + y > b:  # a->b로 옮기는데 b에서 넘쳐남
            q.append([x + y - b, b, z])
        else:  # a->b로 옮기는데 b를 다 못채움
            q.append([0, x + y, z])

        # A->C
        if x + z > c:  # A->C로 옮기는데 C에서 넘쳐남
            q.append([x + z - c, y, c])
        else:  # A->C로 옮기는데 C를 다 못채움
            q.append([0, y, x + z])

        # B->C
        if y + z > c:  # B->C로 옮기는데 C에서 넘쳐남
            q.append([x, y + z - c, c])
        else:  # B->C로 옮기는데 C를 다 못채움
            q.append([x, 0, y + z])

        # B->A
        if y + x > a:  # B->A로 옮기는데 A에서 넘쳐남
            q.append([a, y + x - a, z])
        else:  # B->A로 옮기는데 A를 다 못채움
            q.append([y + x, 0, z])

        # C->A
        if z + x > a:  # C->A로 옮기는데 A에서 넘쳐남
            q.append([a, y, z + x - a])
        else:  # C->A로 옮기는데 A를 다 못채움
            q.append([x + z, y, 0])

        # C->B
        if z + y > b:  # C->B로 옮기는데 B에서 넘쳐남
            q.append([x, b, z + y - b])
        else:  # C->B로 옮기는데 B를 다 못채움
            q.append([x, z + y, 0])


bfs()
for i in range(201):
    if ans[i]:
        print(i, end=' ')

