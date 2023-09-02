import math

n = int(input())
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))
k = int(input())

mainSum = 0
subSum = 0
for i in range(n):
    for j in range(0, n-i-1):
        mainSum += nums[i][j]
    #     print(nums[i][j], end = " ")
    # print()
for i in range(n):
    for j in range(n-i, n):
        subSum += nums[i][j]
    #     print(nums[i][j], end = " ")
    # print()
res = abs(mainSum - subSum)
if res > k: print("NO")
else: print("YES")
print(res)

    
