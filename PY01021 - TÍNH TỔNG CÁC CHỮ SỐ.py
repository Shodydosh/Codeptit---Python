import math

for i in range(int(input())):
    chars = list(input())
    chars.sort()
    ans = 0
    for char in chars:
        if(char <= '9' and char >= '0'):
            ans += (int(char) - int('0'))
        else:
            print(char, end="")
    print(ans)

