def solve(a):
    if min(a) == max(a):
        print("BANG NHAU")
    else:
        print(f"{min(a)} {max(a)}")

while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for _ in range(n):
        a.append(int(input()))
    solve(a)
