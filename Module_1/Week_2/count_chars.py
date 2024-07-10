def count_chars(string):
    """
    Đếm số lần xuất hiện của mỗi ký tự trong chuỗi đầu vào.

    Hàm này duyệt qua từng ký tự trong chuỗi đầu vào và lưu trữ số lần xuất hiện
    của mỗi ký tự vào từ điển.

    Tham số:
    string (str): Chuỗi đầu vào cần đếm ký tự.

    Trả về:
    dict: Từ điển chứa số lần xuất hiện của mỗi ký tự trong chuỗi đầu vào.

    Ví dụ:
    >>> count_chars("Happiness")
    {'H': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}
    >>> count_chars("smiles")
    {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
    """
    char_count = {}
    string = string.lower()
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# Ví dụ
string1 = "Happiness"
string2 = "Helloharry"

print(count_chars(string1))
print(count_chars(string2))
