for _ in range (int(input())):
    n, m = map(int, input().split())
    a, b = [[0] * m] * n, []
    for i in range(n):
        a[i] = list(map(int, input().split()))
    
    for i in range(m):
        x = []
        for j in range(n):
            x += [a[j][i]]
        b.append(x)
    
    for i in range(n):
        for j in range(n):
            s = 0
            for z in range (m):
                s += a[i][z] * b[z][j]
            print(s, end=" ")
        print()
