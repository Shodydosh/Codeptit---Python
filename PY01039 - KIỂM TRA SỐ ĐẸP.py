import math

def solve(num):
    num_str = str(num)
    
    for i in range(0, len(num_str) - 1):
        if i != len(num_str)-2 and num_str[i] != num_str[i + 2]:
            return False
    return True

def main():
    t = int(input())
    while t > 0:
        t -= 1
        a = int(input())
        result = solve(a)
        if(result): print("YES")
        else: print("NO")

if __name__ == "__main__":
    main()
