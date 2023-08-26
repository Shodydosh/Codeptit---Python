import math

def isPrime(a):
    if(a<=1): return False
    if(a<=3): return True
    if(a % 2 == 0 or a % 3 == 0): return False
    sqrt_num = int(math.sqrt(a))
    for i in range(4, sqrt_num +1, 6):
        if a % i == 0 or a % (i+ 2) == 0:
            return False
    return True 

def solve(s):
    if(not isPrime(len(s))): return False
    cnt =0
    for i in range(0, len(s)):
        tmp = ord(s[i]) - ord('0')
        if(isPrime(tmp)):
            cnt+=1
    if cnt > len(s)-cnt: return True 
    else: return False

            
def main():
    t = int(input())
    while t > 0:
        t -= 1
        a = str(input())
        solve(a)
        # print(solve(a))
        if solve(a): print("YES")
        else: print("NO")

if __name__ == "__main__":
    main()
