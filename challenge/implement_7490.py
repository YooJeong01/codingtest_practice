import sys
input = sys.stdin.readline

test_case = int(input())

def solve() :
    global N, answer
    N = int(input())
    answer = []
    select_operator(2, '1') # 1은 고정이고 그 후부터 부호와 숫자에 변수가 생기기 때문에 이렇게 첫 입력을 넣는다
    print()

def select_operator(depth, ans) :
    global answer
    if depth == N+1 :
        set_ans(ans)
        return
    select_operator(depth+1, ans+' '+str(depth)) # 연산자는 3가지가 있기 떄문에 각 경우에 재귀를 호출해 트리 가지뻗기 하는 느낌으로
    select_operator(depth+1, ans+'+'+str(depth))
    select_operator(depth+1, ans+'-'+str(depth))

def set_ans(ans) :
    cal_ans = ans.replace(' ', '')
    if eval(cal_ans) == 0 : # 계산을 해서 0이 되는것만 출력함
        print(ans)

for _ in range(test_case) :
    solve()