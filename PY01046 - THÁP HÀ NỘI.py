import math

def TowerOfHanoi(n, src, des, aux):
    if(n==1):
        print(src + " -> " + des)
        return
    TowerOfHanoi(n-1, src, aux, des)
    print(src + " -> " + des)
    TowerOfHanoi(n-1, aux, des, src)


def main():
    # t = int(input())
    # while t > 0:
    #     t -= 1
        a = int(input())
        A = 'A'
        B = 'B'
        C = 'C'
        TowerOfHanoi(a, A, C, B)
            

if __name__ == "__main__":
    main()
