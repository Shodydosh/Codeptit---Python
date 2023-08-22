import math

def solve(n, k):
    n = int(n)
    k = int(k)
    cnt = 0
    for i in range (pow(10,(k-1)), pow(10,k)):
        if(math.gcd(n, i) == 1):
            print(i, end =' ')
            cnt += 1
            if(cnt == 10): 
                cnt = 0
                print()

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
