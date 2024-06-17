# Viết function lựa chọn regression loss function để tính loss:
import numpy as np
import math


def calculate_regression_loss():
    num_samples = input(
        "Input number of samples ( integer number ) which are generated : "
    )

    # Kiểm tra num_samples có hợp lệ hay không
    if not num_samples.isnumeric():
        print("Số lượng samples phải là một số nguyên.")
        return

    num_samples = int(num_samples)

    loss_name = input("Nhập loại loss function (MAE, MSE, RMSE): ")

    # Dùng vòng lặp để tạo samples và tính toán loss
    for i in range(num_samples):
        predict = np.random.uniform(0, 10)
        target = np.random.uniform(0, 10)

        # Tính toán loss cho từng cặp predict và target
        if loss_name == "MAE":
            loss = abs(predict - target)
        elif loss_name == "MSE":
            loss = (predict - target) ** 2
        elif loss_name == "RMSE":
            loss = math.sqrt((predict - target) ** 2)
        else:
            print("Loss function không hợp lệ. Chỉ có thể là MAE, MSE hoặc RMSE.")
            return

        # In kết quả
        print(f"Sample {i}:")
        print(f"Predict value: {predict}")
        print(f"Target value: {target}")
        print(f"Loss value ({loss_name}): {loss}")


# Gọi hàm để tính toán loss
calculate_regression_loss()
