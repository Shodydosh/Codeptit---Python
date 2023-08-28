def convert(n, b):
    if n == 0:
        return "0"  # Special case when n is 0, the result is "0".

    s = ""
    while n > 0:
        if b > 10:
            remain= n % b
            if remain >=10:
                s = s + str(chr(55 + remain))
            else: 
                s = s + str(remain)
        else:
            s = s + str(n%b)  # Append the remainder as a string to the left.
        n = n // b  # Update n by integer division.
    return "".join(reversed(s))

for i in range(int(input())):
    n, k = list(map(int, input().split()))
    print(convert(n, k))

