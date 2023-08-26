import math

def isPrime(x):
    a = int(x)
    if(a<=1): return False
    if(a<=3): return True
    if(a % 2 == 0 or a % 3 == 0): return False
    sqrt_num = int(math.sqrt(a))
    for i in range(4, sqrt_num +1, 6):
        if a % i == 0 or a % (i+ 2) == 0:
            return False
    return True 

def solve(a):
    str = a
    if(len(a) > 3):
        str = a[len(a) - 3] + a[len(a) - 2] + a[len(a) - 1]
    if(isPrime(int(str))): return True
    return False

def solve2(a):
    str = a
    if(len(a) > 3):
        str = a[0] + a[1] + a[2] 
    if(isPrime(int(str))): return True
    return False
            
def main():
    t = int(input())
    while t > 0:
        t -= 1
        a = str(input())
        # print(solve(a))
        if(solve(a) == True and solve2(a) == True): print("YES")
        else: print("NO")

if __name__ == "__main__":
    main()
