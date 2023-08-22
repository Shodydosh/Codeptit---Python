import math

def solve(a):
    a = int(a)  # Convert the input string to an integer
    a_str_reversed = str(a)[::-1]  # Reverse the string representation of 'a'
    b = int(a_str_reversed)  # Convert the reversed string to an integer
    if math.gcd(a, b) == 1:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    while t > 0:
        a = input()
        solve(a)
        t -= 1

if __name__ == "__main__":
    main()
