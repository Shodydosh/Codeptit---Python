def find_parentheses_pairs(s):
    stack = []
    result = []
    tmp = 1
    for char in s:
        if(char == '('):
            stack.append(tmp);
            result.append(tmp);
            tmp += 1
        elif(char == ')'):
            result.append(stack.pop());
    return result;


for _ in range(int(input())):
    pairs = find_parentheses_pairs(input())
    print(*pairs)
