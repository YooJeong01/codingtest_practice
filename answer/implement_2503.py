import sys

input = sys.stdin.readline

N = int(input())

orders = [list(map(int, input().split())) for _ in range(N)]

count = 0

for i in range(1, 10):          # 첫번째 자리 숫자
    for j in range(1, 10):      # 두번째 자리 숫자
        for k in range(1, 10):  # 세번째 자리 숫자
            if i == j or j == k or i == k: continue # 숫자가 하나라도 중복된다면 건너뜀

            for order in orders:
                n, s, b = order
                x, y, z = map(int, str(n)) # x:첫번째 자리 / y:두번째 자리 / z: 세번째 자리

                count_s, count_b = 0, 0

                if x == i:
                    count_s += 1            # 첫 번째 자리 숫자와 똑같다면 strike +1
                elif (y == i or z == i):    # 두번째, 세번째 자리 숫자와 같다면 ball +1
                    count_b += 1

                if y == j:
                    count_s += 1
                elif (x == j or z == j):
                    count_b += 1

                if z == k:
                    count_s += 1
                elif (x == k or y == k):
                    count_b += 1

                if not (s == count_s and b == count_b):
                    break
            else:
                count += 1

print(count)