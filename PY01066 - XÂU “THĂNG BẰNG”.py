import math

def solve(b):
    a = b[::-1]
    for i in range(1, len(a)):
        if(abs(ord(a[i])-ord(a[i-1])) != abs(ord(b[i])-ord(b[i-1]))):
            return False
    return True

def main():
    t = int(input())
    while t > 0:
        t -= 1
        b = str(input())
        if solve(b):
            print("YES")
        else:
            print("NO")
if __name__ == "__main__":
    main()
