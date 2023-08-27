def count_steps_to_equal(A):
    steps = 0
    
    while len(set(A)) > 1:
        new_A = []
        for i in range(len(A)):
            if i == len(A) - 1:
                new_A.append(abs(A[i] - A[0]))
            else:
                new_A.append(abs(A[i] - A[i + 1]))
        A = new_A
        steps += 1
    
    return steps

while True:
    A = list(map(int, input().split()))
    if A == [0, 0, 0, 0]:
        break
    result = count_steps_to_equal(A)
    print(result)
