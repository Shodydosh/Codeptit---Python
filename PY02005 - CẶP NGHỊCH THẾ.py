import math
n = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(0, len(arr)):
    for j in range(i, len(arr)):
        if(arr[i] > arr[j]): ans+=1
print(ans)
