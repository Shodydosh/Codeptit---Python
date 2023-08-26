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
    if(len(a) % 2 == 0): return False
    chars = [char for char in a]
    for i in range(0, len(a)-2, 2):
        if(chars[i] != chars[i+2]): return False
    return True
            
def main():
    t = int(input())
    while t > 0:
        t -= 1
        a = str(input())
        if(solve(a) == True): print("YES")
        else: print("NO")

if __name__ == "__main__":
    main()
