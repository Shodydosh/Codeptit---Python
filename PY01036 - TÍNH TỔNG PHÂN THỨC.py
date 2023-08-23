import math

def cal(N):
    S = 0
    if N % 2 == 1:  # N là số lẻ
        for i in range(1, N + 1, 2):
            S += 1/i
    else:  # N là số chẵn
        for i in range(2, N + 1, 2):
            S += 1/i
    return round(S, 6)                

def main():
    t = int(input())
    while t > 0:
        t -= 1
        a = int(input())
        result = cal(a)
        print(f'{result:.6f}')

if __name__ == "__main__":
    main()
