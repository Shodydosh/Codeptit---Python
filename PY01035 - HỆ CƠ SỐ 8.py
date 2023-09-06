def solve(s):
    res = ""
    i = 0
    while i < len(s):
        tmp = int(s[i]) * 4 + int(s[i+1]) * 2 + int(s[i+2])
        res += str(tmp)
        i+=3
    return res

s = input()
tmp = len(s) % 3
if tmp >0 :
    for _ in range(3-tmp):
        s = '0' + s
print(solve(s))
