def levenshtein_distance(source, target):
    m = len(source)
    n = len(target)

    # Khởi tạo ma trận (m+1) x (n+1)
    D = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Điền giá trị cho hàng đầu tiên và cột đầu tiên
    for i in range(m + 1):
        D[i][0] = i
    for j in range(n + 1):
        D[0][j] = j

    # Tính toán các giá trị cho các ô còn lại
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            D[i][j] = min(D[i - 1][j] + 1,  # Xóa
                          D[i][j - 1] + 1,  # Chèn
                          D[i - 1][j - 1] + substitution_cost)  # Thay thế

    # Giá trị khoảng cách Levenshtein nằm ở ô cuối cùng của ma trận
    return D[m][n]


# Ví dụ
source = "kitten"
target = "sitting"

# Gọi hàm và in kết quả
distance = levenshtein_distance(source, target)
print(f"Khoảng cách Levenshtein giữa '{source}' và '{target}' là {distance}")
