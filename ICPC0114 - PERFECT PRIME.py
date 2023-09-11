def cal(n):
    x = 0
    for i in range(0, len(n)):
        x += int(n[i])
    return x

def check(n):
    for i in range(0, len(n)):
        if(n[i] != '2' and n[i] != '3' and n[i] != '5' and n[i] != '7'):
            return False
    return True

def isPrime(x):
    a = int(x)
    if(a<=1): return False
    if(a<=3): return True
    if(a % 2 == 0 or a % 3 == 0): return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

for _ in range(int(input())):
    n = input()
    sum = cal(n)
    if isPrime(sum) and isPrime(int(n)) and isPrime(int(n[::-1])) and check(n):
        print("Yes")
    else:
        print("No")   
    
