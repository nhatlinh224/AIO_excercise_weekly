# Viết function thực hiện đánh giá classification model bằng F1-Score
def calculate_f1_score(tp, fp, fn):
    # Kiểm tra kiểu dữ liệu của tp, fp, fn
    if not isinstance(tp, int):
        print("tp must be int")
        return

    if not isinstance(fp, int):
        print("fp must be int")
        return

    if not isinstance(fn, int):
        print("fn must be int")
        return

    # Kiểm tra giá trị của tp, fp, fn lớn hơn 0
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return

    # Tính toán Precision, Recall, và F1-score
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    # In kết quả
    print(f"precision is {precision:.1f}")
    print(f"recall is {recall}")
    print(f"f1-score is {f1_score}")


# Test calculate_f1_score
calculate_f1_score(2, 3, 4)
