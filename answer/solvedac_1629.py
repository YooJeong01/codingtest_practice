# 4 * 4 * 4 * 4 =256 \
#                % 6 = 4
#                 % 3 = 1
# 4 * 4 * 4 * 4 * 4 = 1024 \
#                     % 6 = 4
#                     % 3 = 1
#
# 10 * 10 * 10 = 1000 % 12 = 4
# 10 * 10 = 100 % 12 = 4
# 10 * 10 * 10 * 10 * 10 = 100000

# 분할정복을 통한 제곱수를 구하는 방식
# 모듈러 연산 성질
# or 파이썬 내장 함수 pow() 사용

a, b, c = map(int, input().split())
# print(pow(a, b, c))
def solution(a, b, c):
    if b == 1:
        return a % c

    temp = solution(a, b // 2, c)

    if b % 2 == 1:
        return ((temp * temp) % c) * a % c
    else:
        return (temp * temp) % c
print(solution(a, b, c))