def mean_difference_nth_root_error():
    y = input("nhập giá trị của y: ")
    y_hat = input("nhập giá trị của y_hat: ")
    n = input("nhập giá trị của n: ")
    p = input("nhập giá trị của p: ")

    y = float(y)
    y_hat = float(y_hat)
    n = float(n)
    p = float(p)

    md_nre = (y ** (1 / n) - y_hat ** (1 / n)) ** p
    return md_nre


# Excercise Test
print(mean_difference_nth_root_error())
