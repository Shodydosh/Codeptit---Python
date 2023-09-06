def solve(s1, s2):
    if len(s1) != len(s2):
        return "NO"
    
    c1 = [char for char in s1]
    c2 = [char for char in s2]
    c1.sort()
    c2.sort()
    if c1 == c2: return "YES"
    else: return "NO"

for i in range(int(input())):
    s1 = input()
    s2 = input()
    print("Test", i+1, end = ": ")
    print(solve(s1, s2)) 
