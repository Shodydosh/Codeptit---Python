import math

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = nums[len(nums)-1] + 1
for i in range(1, len(nums)):
    if(nums[i] - nums[i-1] > 1):
        ans = nums[i-1] + 1
        break
print(ans)
