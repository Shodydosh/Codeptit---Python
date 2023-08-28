def convert(n):
    re = len(n)%3
    if(re > 0): 
        for i in range(0, 3-re):
            n = '0' + n
    for i in range(0, len(n), 3):
        s = 4 * int(n[i]) + 2 * int(n[i+1]) +  int(n[i+2])
        print(s, end ="")
    return ""

print(convert(input()))

