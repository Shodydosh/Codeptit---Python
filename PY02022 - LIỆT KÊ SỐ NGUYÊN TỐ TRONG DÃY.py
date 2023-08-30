import math

def isPrime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while(i * i < n):
        if(n % i == 0 or n % (i+2) == 0):
            return False
        i += 6
    return True

count = {}
n = int(input())
nums = list(map(int, input().split()))
for num in nums:
    if isPrime(num):
        if num not in count:
            count[num] = 0
        count[num] += 1
for x in count:
    print(x, count[x])
