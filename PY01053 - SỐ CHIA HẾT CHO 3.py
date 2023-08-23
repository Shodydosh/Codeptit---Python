import math

def cal(num):
    sum = 0
    for i in range (0, len(num)):
        sum += int(num[i])
    if((sum % 3 == 0)): return True
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
