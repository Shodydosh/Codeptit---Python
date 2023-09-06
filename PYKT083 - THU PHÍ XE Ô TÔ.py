
def tinh_phi(xe, seat):
    seat = int(seat)
    if xe == "Xe_con" and seat == 5: return 10000
    if xe == "Xe_con" and seat == 7: return 15000
    if xe == "Xe_khach" and seat == 29: return 50000
    if xe == "Xe_khach" and seat == 45: return 70000
    return 20000

# Khởi tạo một từ điển để lưu trữ thông tin về các chủ đề và số lượng câu hỏi tương ứng
curr_date = ''
system = {}

# Iterate through each line of input
for _ in range(int(input())):
    bs, xe, seat, direction, date = input().split(' ')

    if direction == 'IN':
        if date != curr_date or curr_date == '':
            curr_date = date
            system[curr_date] = 0

        # Assuming tinh_phi(xe, seat) calculates the fee based on xe and seat
        system[curr_date] += tinh_phi(xe, seat)

# Iterate through the system dictionary and print fees for each date
for date, phi in system.items():
    print(f"{date}: {phi}")
