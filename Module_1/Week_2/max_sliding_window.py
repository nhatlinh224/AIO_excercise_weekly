def max_sliding_window(num_list, k):
    n = len(num_list)
    if n * k == 0:
        return []

    if k == 1:
        return num_list

    def clean_deque(i):
        # Remove indexes of elements not from sliding window
        if deq and deq[0] == i - k:
            deq.pop(0)

        # Remove from deq indexes of all elements
        # which are smaller than current element num_list[i]
        while deq and num_list[i] > num_list[deq[len(deq) - 1]]:
            deq.pop()

    # Init deque and output
    deq = []
    max_idx = 0
    for i in range(k):
        clean_deque(i)
        deq.append(i)
        # Compute max in num_list[:k]
        if num_list[i] > num_list[max_idx]:
            max_idx = i
    output = [num_list[max_idx]]

    # Build output
    for i in range(k, n):
        clean_deque(i)
        deq.append(i)
        output.append(num_list[deq[0]])
    return output


# Đầu vào
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3

# Gọi hàm và in kết quả
output = max_sliding_window(num_list, k)
print(output)
