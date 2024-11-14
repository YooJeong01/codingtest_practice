N = int(input())
nums = []
for i in range(1,N+1) :
    nums.append(i)
result = []
for i in range(N-1) :
    top_card = nums.pop(0)
    result.append(top_card)
    second_card = nums.pop(0)
    nums.append(second_card)
result.append(nums[0])
print(*result)