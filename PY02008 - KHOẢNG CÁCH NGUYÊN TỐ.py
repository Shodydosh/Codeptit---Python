import math

prime = [0] * 100005
def render():
    prime[0] = prime[1] = 1
    for i in range(2, int(math.sqrt(100005))+1):
        if(prime[i] == 0):
            for j in range(i * i, 100005, i):
                prime[j] = 1
render()
a = [0]
for i in range(100005):
    if(prime[i] == 0): 
        a.append(a[len(a)-1] + i)

n, x = map(int, input().split())
for i in range(0, n+1):
    print(x + a[i], end = ' ')
