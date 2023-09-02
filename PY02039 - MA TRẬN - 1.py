import math

n = int(input())
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))
k = int(input())

mainSum = 0
subSum = 0
for i in range(n):
    for j in range(i, n):
        mainSum += nums[i][j]
    #     print(nums[i][j], end = " ")
    # print()
for i in range(n):
    for j in range(0, i+1):
        subSum += nums[i][j]
        # print(nums[i][j], end = " ")
    # print()
res = abs(mainSum - subSum)
if res > k: print("NO")
else: print("YES")
print(res)

    
