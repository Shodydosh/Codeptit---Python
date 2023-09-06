import math

def solve(a, b, c, d):
    resA = a*d + b*c
    resB = b * d
    return (resA//math.gcd(resA, resB), resB//math.gcd(resA, resB))

a, b, c, d = map(int, input().split())
res = solve(a, b, c, d)
print(str(res[0]) + '/' + str(res[1]))
