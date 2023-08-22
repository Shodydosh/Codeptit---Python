import math

def solve(a):
    chars = list(a)
    cnt = 0
    for i in range(len(chars) - 1, -1, -1):
        cnt+=1
        if cnt == 3 and i != 0: 
            chars.insert(i, ',')
            cnt = 0
    result = ''.join(chars)
    return result

def main():
    # t = int(input())
    # while t > 0:
        a = input()
        print(solve(a))  # Removed the print statement here
        # t -= 1  # Decremented the loop counter

if __name__ == "__main__":
    main()
