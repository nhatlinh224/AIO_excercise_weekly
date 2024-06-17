def word_count(file_path):
    # Dictionary để lưu trữ số lượng xuất hiện của các từ
    word_count_dict = {}

    # Đọc file và xử lý từng dòng
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Loại bỏ các ký tự không phải chữ và chuyển thành chữ thường
            words = line.lower().split()
            for word in words:
                # Loại bỏ dấu câu
                word = ''.join(char for char in word if char.isalpha())
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1

    return word_count_dict


# Đường dẫn đến file txt
file_path = '/mnt/data/P1_data.txt'

# Gọi hàm và in kết quả
output = word_count(file_path)
print(output)
