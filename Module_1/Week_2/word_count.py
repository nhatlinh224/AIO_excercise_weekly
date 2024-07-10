# Đường dẫn đến file txt
import os

# Lấy đường dẫn tuyệt đối của thư mục hiện tại
current_dir = os.path.dirname(os.path.abspath(__file__))

# Kết hợp với tên file để tạo đường dẫn tuyệt đối
file_path = os.path.join(current_dir, 'data/P1_data.txt')

with open(file_path, 'r') as f:
    sentences = f.readlines()
print(sentences)


def preprocess_text(sentence):
    """
    Chuyển đổi chuỗi thành chữ thường, loại bỏ dấu chấm và dấu phẩy,
    sau đó tách chuỗi thành các từ.

    Tham số:
    sentence (str): Chuỗi đầu vào cần xử lý.

    Trả về:
    list: Danh sách các từ sau khi xử lý.
    """
    sentence = sentence.lower()
    sentence = sentence.replace('.', '').replace(',', '')
    words = sentence.split()
    return words


# Đếm số lần xuất hiện của các từ trong danh sách các câu
counter = {}
for sentence in sentences:
    words = preprocess_text(sentence)
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

print(counter)
