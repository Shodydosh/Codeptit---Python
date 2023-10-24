def solve(a, n):
    res = []
    for i in a:
        tmp = 0
        for j in a:
            tmp += abs(j - i);
        res.append(tmp)
    print(f"{min(res)} {a[res.index(min(res))]}")

n = int(input())
a = [int(x) for x in input().split()]
solve(a, n)
