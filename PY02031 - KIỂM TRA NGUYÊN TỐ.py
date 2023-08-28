import math
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def replace_prime_numbers(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if is_prime(matrix[i][j]):
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

matrix = []
m, n = list(map(int, input().split()))
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
replace_prime_numbers(matrix)

for row in matrix:
    for num in row:
        print(num, end = ' ')
    print()
