import math
from itertools import permutations

while True:
    N = int(input())
    
    if N == 0:
        break
    
    seen = set()  # Sử dụng một set để lưu trữ các giá trị đã xuất hiện
    count = 0
    
    while N != 1:
        # Nếu N đã xuất hiện trước đó, thì dừng vòng lặp
        if N in seen:
            break
        seen.add(N)
        
        # Thực hiện phép biến đổi
        if N % 2 == 0:
            N = N // 2
        else:
            N = N * 3 + 1
        
        count += 1
    
    # Đếm số lượng giá trị đã xuất hiện và in ra kết quả
    print(count + 1)
