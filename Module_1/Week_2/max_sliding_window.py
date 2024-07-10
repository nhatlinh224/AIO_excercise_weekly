# Solution 1
def max_sliding_window(num_list, k):
    """
    This function calculates the maximum value in each sliding window of size `k` in the input list `num_list`.

    Parameters:
    num_list (list): A list of integers.
    k (int): The size of the sliding window.

    Returns:
    list: A list of integers representing the maximum value in each sliding window.
    """
    result = []
    sliding_window = []

    for element in num_list:
        sliding_window.append(element)

        if len(sliding_window) == k:
            result.append(max(sliding_window))
            del sliding_window[0]

    return result


# TestCase
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_sliding_window(num_list, k))


# Slicing Solution 2
def max_sliding_window2(num_list, k):
    if k < 1:
        raise ValueError("k phải lớn hơn hoặc bằng 1")

    start_indexes = list(range(0, len(num_list) - k + 1))
    end_indexes = list(range(k, len(num_list) + 1))
    result = []

    for start_index, end_index in zip(start_indexes, end_indexes):
        sub_list = num_list[start_index:end_index]
        result.append(max(sub_list))

    return result


# Test Case
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_sliding_window2(num_list, k))
