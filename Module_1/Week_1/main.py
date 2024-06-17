from activation_function import check_activation_function, sigmoid, relu, elu
from calculate_f1_score import calculate_f1_score
from estimate_sin_cos_sinh_cosh import (
    estimate_sin,
    estimate_cos,
    estimate_sinh,
    estimate_cosh,
)
from mean_difference_nth_root_error import mean_difference_nth_root_error
from regression_loss_function import calculate_regression_loss


def main():
    while True:
        print("\nChọn chức năng bạn muốn thực hiện:")
        print("1. Tính toán activation function")
        print("2. Tính toán F1 Score")
        print("3. Ước lượng sin, cos, sinh, cosh")
        print("4. Tính Mean Difference of nth Root Error")
        print("5. Tính Regression Loss")
        print("6. Thoát")

        choice = input("Nhập lựa chọn của bạn (1-6): ")

        if choice == "1":
            name = input("Nhập tên activation function (sigmoid, relu, elu): ")
            if check_activation_function(name):
                x = float(input("Nhập giá trị của x: "))
                if name == "sigmoid":
                    print(f"Kết quả của sigmoid({x}) là {sigmoid(x)}")
                elif name == "relu":
                    print(f"Kết quả của relu({x}) là {relu(x)}")
                elif name == "elu":
                    print(f"Kết quả của elu({x}) là {elu(x)}")

        elif choice == "2":
            tp = int(input("Nhập số lượng true positive: "))
            fp = int(input("Nhập số lượng false positive: "))
            fn = int(input("Nhập số lượng false negative: "))
            calculate_f1_score(tp, fp, fn)

        elif choice == "3":
            x = float(input("Nhập giá trị của x: "))
            n = int(input("Nhập giá trị của n: "))
            print(f"estimate_sin({x}, {n}) = {estimate_sin(x, n)}")
            print(f"estimate_cos({x}, {n}) = {estimate_cos(x, n)}")
            print(f"estimate_sinh({x}, {n}) = {estimate_sinh(x, n)}")
            print(f"estimate_cosh({x}, {n}) = {estimate_cosh(x, n)}")

        elif choice == "4":
            y = input("Nhập giá trị của y (các giá trị cách nhau bởi dấu cách): ")
            y_hat = input(
                "Nhập giá trị của y_hat (các giá trị cách nhau bởi dấu cách): "
            )
            n = input("Nhập giá trị của n: ")
            p = input("Nhập giá trị của p: ")
            result = mean_difference_nth_root_error(y, y_hat, n, p)
            print("MD_nRE (n = {}, p = {}):".format(n, p), result)

        elif choice == "5":
            calculate_regression_loss()

        elif choice == "6":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()
