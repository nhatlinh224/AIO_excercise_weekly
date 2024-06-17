def count_chars(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# Ví dụ
string1 = "Happiness"
string2 = "smiles"

# Gọi hàm và in kết quả
output1 = count_chars(string1)
output2 = count_chars(string2)

print(output1)
print(output2)
