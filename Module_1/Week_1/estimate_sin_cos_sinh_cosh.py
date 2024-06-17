import math


def factorial(number):
    if number == 0 or number == 1:
        return 1
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


def estimate_sin(x, n):
    result = 0
    for i in range(n):
        values = ((-1) ** i) * (pow(x, (2 * i + 1))) / factorial(2 * i + 1)
        result += values
    return result


def estimate_cos(x, n):
    result = 0
    for i in range(n):
        values = ((-1) ** i) * (pow(x, (2 * i))) / factorial(2 * i)
        result += values
    return result


def estimate_sinh(x, n):
    result = 0
    for i in range(n):
        values = pow(x, (2 * i + 1)) / factorial(2 * i + 1)
        result += values
    return result


def estimate_cosh(x, n):
    result = 0
    for i in range(n):
        values = pow(x, (2 * i)) / factorial(2 * i)
        result += values
    return result


def values():
    x = float(input("Nhập giá trị của x: "))

    # Kiểm tra x có nằm trong khoảng hợp lý hay không
    if x < -2 * math.pi or x > 2 * math.pi:
        print("x phải nằm trong khoảng từ -2π đến 2π.")
        return

    n = input("Nhập giá trị của n: ")

    # Kiểm tra nếu n là số nguyên dương
    try:
        inter_n = int(n)
        if str(inter_n) != n or int(n) <= 0:
            print("n phải là số nguyên dương lớn hơn 0.")
    except ValueError:
        print("n phải là số nguyên dương lớn hơn 0.")
        return

    # Chuyển đổi n thành số nguyên để sử dụng trong các phép tính
    n = int(n)

    print(estimate_sin(x, n))
    print(estimate_cos(x, n))
    print(estimate_sinh(x, n))
    print(estimate_cosh(x, n))


values()
