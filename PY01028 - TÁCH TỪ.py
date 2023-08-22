import math

def solve(a):
    split_list = a.split()  # Splits by space
    for word in split_list:
        print(word)

def main():
    # t = int(input())
    # while t > 0:
        a = input()
        solve(a)  # Removed the print statement here
        # t -= 1  # Decremented the loop counter

if __name__ == "__main__":
    main()
