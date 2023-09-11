def check(n) :
    if n[-1] == n[0]: return True
    else: return False

for _ in range(int(input())):
    n = (input())
    if(check(n)): print("YES")
    else: print("NO")
