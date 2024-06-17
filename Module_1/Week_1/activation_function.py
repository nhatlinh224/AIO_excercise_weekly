# Viết function mô phỏng theo 3 activation function


# Kiểm tra x có hợp lệ hay không
import math


def is_number(n):
    try:
        float(n)  # Type - casting the string to ‘float ‘.
        # If string is not a valid ‘float ‘ ,
        # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


# Kiểm tra activation function name có hợp lệ hay không nằm trong 3 tên (sigmoid, relu, elu)


def check_activation_function(name):
    valid_function = {"sigmoid", "relu", "elu"}

    if name not in valid_function:
        print(f"{name} is not supported")
        return False
    return True


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    if x >= 0:
        return 0
    return x


def elu(x, alpha=0.01):
    if x > 0:
        return x
    return alpha * (math.exp(x) - 1)


def apply_activation_function(function_name, x):
    if not check_activation_function(function_name):
        print(f"{function_name} is not supported")
        return

    if not is_number(x):
        print(f"{x} must be a number")
        return

    x = float(x)

    if function_name == "sigmoid":
        result = sigmoid(x)
    elif function_name == "relu":
        result = relu(x)
    elif function_name == "elu":
        result = elu(x)

    print(f"Kết quả của {function_name}({x}) là {result}")


# Ví dụ sử dụng hàm
apply_activation_function("sigmoid", 0.5)
apply_activation_function("relu", -1)
apply_activation_function("elu", -1)
apply_activation_function("belu", 0.5)
apply_activation_function("sigmoid", "abc")
