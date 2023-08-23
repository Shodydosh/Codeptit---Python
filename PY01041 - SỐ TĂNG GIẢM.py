import math

def solve(num):
    num_str = str(num)
    
    # Kiểm tra nếu số có ít nhất 3 chữ số
    if len(num_str) < 3:
        return False
    
    # Kiểm tra từ bên trái đến vị trí đầu tiên thỏa mãn tăng dần
    for i in range(1, len(num_str)):
        if num_str[i] <= num_str[i - 1]:
            break
    else:
        return False  # Không tìm thấy vị trí thỏa mãn tăng dần
    
    for i in range(i + 1, len(num_str)):
        if num_str[i] >= num_str[i - 1]:
            return False
    
    return True

def main():
    t = int(input())
    while t > 0:
        t -= 1
        a = int(input())
        result = solve(a)
        if(result): print("YES")
        else: print("NO")

if __name__ == "__main__":
    main()
