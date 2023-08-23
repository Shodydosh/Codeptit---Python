import math

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def cal(num):
    sum = 0
    for i in range (0, len(num)):
        sum += int(num[i])
    if(is_prime(sum)): return True
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
