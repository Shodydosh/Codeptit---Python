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
    if (isPrime(len(a))):
        cnt = 0
        for i in a:
            if isPrime(int(i)) == False:
                cnt += 1
        return cnt < len(a) - cnt
    return False
            
def main():
    t = int(input())
    while t > 0:
        t -= 1
        a = str(input())
        if(solve(a) == True): print("YES")
        else: print("NO")

if __name__ == "__main__":
    main()
