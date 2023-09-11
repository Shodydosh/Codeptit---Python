a = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
def check(n) :
    s = 0
    m = n
    while n > 0 :
        s += a[n % 10]
        n = int(n / 10)
    if s == m : return True
    else : return False

for _ in range(int(input())):
    n = int(input())
    if(check(n)): print("Yes")
    else: print("No")
