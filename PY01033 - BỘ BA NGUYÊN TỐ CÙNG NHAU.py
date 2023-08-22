import math

def solve(n, k):
    n = int(n)
    k = int(k)
    cnt = 0
    for i in range (n, k-1):
        for j in range (i+1, k):
            for q in range (j+1, k+1):
                if(math.gcd(i, j) == 1 and math.gcd(j, q) == 1 and math.gcd(i, q) == 1):
                    print("(" + str(i) + ", " + str(j) + ", " + str(q) + ")")

def main():
    # t = int(input())
    # while t > 0:
        # t -= 1
        inn = input()
        numbers = inn.split()
        n = numbers[0]
        k = numbers[1]
        solve(n, k)

if __name__ == "__main__":
    main()
