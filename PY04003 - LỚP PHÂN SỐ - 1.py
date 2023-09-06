import math
def rut_gon(a, b):
    return (a//math.gcd(a, b), b//math.gcd(a, b))

a, b = map(int, input().split())
res = rut_gon(a, b) 
print(str(res[0]) + '/' + str(res[1]))
