import math
from itertools import permutations



def solve(b):
    a = b[::-1]
    for i in range(1, len(a)):
        if(abs(ord(a[i])-ord(a[i-1])) != abs(ord(b[i])-ord(b[i-1]))):
            return False
    return True

def main():
    # t = int(input())
    # while t > 0:
    #     t -= 1
        b = str(input())
        permutations_list = permutations(b)

        for perm in permutations_list:
            print("".join(perm))
if __name__ == "__main__":
    main()
