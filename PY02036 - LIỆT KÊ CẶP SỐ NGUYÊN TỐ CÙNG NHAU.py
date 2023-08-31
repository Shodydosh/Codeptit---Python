import math

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
for i in range (0, len(nums)):
    for j in range (i+1, len(nums)):
        if(math.gcd(nums[i], nums[j]) == 1):
            print(nums[i], nums[j])
