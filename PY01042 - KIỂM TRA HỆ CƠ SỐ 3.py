import math

def solve(a):
    chars = [char for char in a]
    for i in range(len(chars)):
        if(chars[i] != '0' and chars[i] != '1' and chars[i] != '2'):
            return "NO"
    return "YES"

def main():
    t = int(input())
    while t > 0:
        t -= 1
        a = (input())
        print(solve(a))

if __name__ == "__main__":
    main()
