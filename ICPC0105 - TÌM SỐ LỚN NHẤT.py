
for _ in range(int(input())):
    max_val = 0
    tmp = 0
    chars = list(c for c in input())
    chars.append('z')
    for char in chars:
        if(char.isdigit()):
            tmp = tmp * 10 + int(char)
        else:
            if tmp > 0:
                if max_val < tmp: max_val = tmp
                tmp = 0
    print(max_val)
