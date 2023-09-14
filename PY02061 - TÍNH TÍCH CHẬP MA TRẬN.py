for _ in range(int(input())):
    m, n = map(int, input().split())
    # print(m, n, m+n)
    matA = []
    matK = []
    for i in range (m):
        tmp = list(map(int, input().split()))
        matA.append(tmp)
    for i in range (3):
        tmp = list(map(int, input().split()))
        matK.append(tmp)

    ans = 0
    for i in range(m - 2):
        for j in range(n - 2):
            tmp = 0
            for x in range(3):
                for y in range(3):
                    tmp += matA[i+x][j+y] * matK[x][y]
            ans += tmp
    print(ans)
