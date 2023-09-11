a = [0] * 1000001

def check(n):
    if(a[n] == 0 and a[n+2] == 0 and a[n+6] == 0): return True
    if(a[n] == 0 and a[n+4] == 0 and a[n+6] == 0): return True
    return False

def era() :
    a[0] = a[1] = 1
    for i in range(2, 1000) :
        if a[i] == 0 :
            for j in range(i * i, 1000001, i) : a[j] = 1
era()
for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(1, n-6):
        if(check(i)):
            cnt+=1
    print(cnt)
