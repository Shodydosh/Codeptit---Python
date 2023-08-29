import math

n = int(input())
nums = list(map(int, input().split(' ')))
cur = nums[0]
ans = 0
for i in range (1, len(nums)):
    if nums[i] != cur: 
        ans += 1
        cur = nums[i]
print(ans)
