import math

nums = []
while(len(nums) < 10):
    nums += list(map(int, input().split()))
res = [num % 42 for num in nums]
res.sort()
ans = 10
for i in range (0,9):
    if(res[i] == res[i+1]): ans -= 1
print(ans)
