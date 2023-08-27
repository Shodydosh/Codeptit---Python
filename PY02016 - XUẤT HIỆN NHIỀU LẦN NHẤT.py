from collections import defaultdict

def find_majority_element(N, A):
    # Sử dụng defaultdict để đếm tần số xuất hiện của từng số
    count = defaultdict(int)
    
    for num in A:
        count[num] += 1
    
    # Duyệt qua từng số trong dãy
    for num in A:
        if count[num] > N // 2:
            return num
    
    return "NO"

# Đọc số lượng test cases
T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    result = find_majority_element(N, A)
    print(result)
