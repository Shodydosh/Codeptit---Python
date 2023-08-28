import math

s1 = input()
s2 = input()
k = int(input())
for i in range(0, len(s1)):
    if(i == k-1):
        print(s2, end='')
    print(s1[i], end='')
if(k-1 == len(s1)): print(s2)
