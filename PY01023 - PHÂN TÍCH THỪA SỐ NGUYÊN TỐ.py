import math

def solve(a):
    a = int(a)
    ans = "1"
    if a > 1:
        for i in range(2, math.ceil(a/2) + 1):  # Fixed the range and added 1
            if a % i == 0:
                cnt = 0
                while a % i == 0:
                    cnt += 1
                    a /= i
                if cnt != 0:
                    ans += (" * " + str(i) + "^" + str(cnt))
    if a != 1:
        return ans + " * " + str(a) + "^1"
    return ans

def main():
    t = int(input())
    while t > 0:
        a = int(input())
        print(solve(a))  # Removed the print statement here
        t -= 1  # Decremented the loop counter

if __name__ == "__main__":
    main()
