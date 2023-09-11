ss = {}
for _ in range(int(input())):
    s = (input())
    if s not in ss:
        ss[s] = 1
print(len(ss))
