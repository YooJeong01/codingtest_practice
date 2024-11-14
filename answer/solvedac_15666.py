# point :
# 중복수열 방지
# 입력에서 중복되는 원소가 주어질때, 중복되는 조합은 가능하고, 중복수열은 불가능하다면
# 이전값을 기억하도록 코드를 짠다!

n, m = map(int, input().split())
nums = list(map(int, input().split()))
arr = []
nums.sort()

def backtracking(start) :
    if len(arr) == m :
        print(' '.join(map(str, arr)))
        return

    remember_me = 0
    for i in range(start, n) :
        if remember_me != nums[i] :
            arr.append(nums[i])
            remember_me = nums[i]
            backtracking(i)
            arr.pop()

backtracking(0)
