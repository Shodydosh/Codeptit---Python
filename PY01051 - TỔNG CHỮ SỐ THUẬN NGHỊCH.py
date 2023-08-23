import math

def isPal(num):
    if(len(str(num)) <= 1): return False
    else:
        if(str(num) != str(num)[::-1]):
            return False
    return True

def cal(num):
    sum = 0
    for i in range (0, len(num)):
        sum += int(num[i])
    if(isPal(sum)): return True
    else: return False

def main():
    t = int(input())
    while t > 0:
        t -= 1
        a = input()
        result = cal(a)
        if(result): print("YES")
        else: print("NO")

if __name__ == "__main__":
    main()
