import math

n = int(input())
arr = list(map(int, input().split()))
b = []
for num in arr:
    if(len(b) == 0):
        b = b + [num]
    else:
        if(b[-1] + num) % 2 == 0:
            b.pop()
        else:
            b = b + [num]
print(len(b))
