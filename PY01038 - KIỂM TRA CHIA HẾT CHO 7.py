import math

def solve(n):
    cnt = 0
    while(cnt <= 1000):
        if(n%7 == 0): break
        n += int(str(n)[::-1])
        cnt+=1
    if(cnt <= 1000): return n
    else: return -1

def main():
    t = int(input())
    while t > 0:
        t -= 1
        a = int(input())
        result = solve(a)
        print(result)

if __name__ == "__main__":
    main()
