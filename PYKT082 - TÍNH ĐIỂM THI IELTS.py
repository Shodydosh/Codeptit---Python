import math

def cal1(a):
    if(a <= 4): return 2.5
    if(a <= 6): return 3.0
    if(a <= 9): return 3.5
    if(a <= 12): return 4.0
    if(a <= 15): return 4.5
    if(a <= 19): return 5.0
    if(a <= 22): return 5.5
    if(a <= 26): return 6.0
    if(a <= 29): return 6.5
    if(a <= 32): return 7.0
    if(a <= 34): return 7.5
    if(a <= 36): return 8.0
    if(a <= 38): return 8.5
    return 9.0

def cal2(a, b, c, d):
    tmp = (a+b+c+d)/4
    if(tmp - math.floor(tmp) >= 0.75): return math.floor(tmp) + 1.0
    if(tmp - math.floor(tmp) < 0.25): return float(math.floor(tmp))
    return math.floor(tmp) + 0.5

for i in range(int(input())):
    a, b, c, d = list(map(float, input().split()))
    a, b = int(a), int(b)
    a, b = cal1(a), cal1(b)
    print(cal2(a, b, c, d))
