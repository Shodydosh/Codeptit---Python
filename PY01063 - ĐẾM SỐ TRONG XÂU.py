import math

def main():
    t = int(input())
    while t > 0:
        t -= 1
        a = str(input())
        b = str(input())
        print(a.count(b))

if __name__ == "__main__":
    main()
