
for _ in range(int(input())):
    min_val = -1
    tmp = 0
    chars = list(c for c in input())
    chars.append('z')
    for char in chars:
        if(char.isdigit()):
            tmp = tmp * 10 + int(char)
        else:
            if tmp > 0:
                if min_val == -1: min_val = tmp
                elif min_val > tmp: min_val = tmp
                tmp = 0
    print(min_val)
