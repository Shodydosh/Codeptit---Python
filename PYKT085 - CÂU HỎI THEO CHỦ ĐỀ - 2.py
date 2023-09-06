# Đọc tổng số dòng dữ liệu
total_lines = int(input())
# Khởi tạo một từ điển để lưu trữ thông tin về các chủ đề và số lượng câu hỏi tương ứng
topic_questions = {}
current_topic = ""

# Duyệt qua từng dòng dữ liệu
for _ in range(total_lines):
    line = input().strip()
    
    # Kiểm tra xem dòng hiện tại có phải là chủ đề mới hay không
    if not line:
        current_topic = ""
    elif current_topic == "":
        current_topic = line
        topic_questions[current_topic] = 0
    else:
        topic_questions[current_topic] += 1

for topic, num_questions in topic_questions.items():
    print(f"{topic}: {num_questions}")
