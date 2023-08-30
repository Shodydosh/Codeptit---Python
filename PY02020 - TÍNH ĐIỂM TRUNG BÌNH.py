import math

n = int(input())
nums = list(map(float, input().split()))
cnt = 0
All_sum = 0
for i in range(0, len(nums)):
    if(nums[i] != min(nums) and nums[i] != max(nums)):
        cnt += 1
        All_sum = All_sum + nums[i]
average = round(All_sum / cnt, 2)
print(average)
