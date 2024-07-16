class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if self.is_full():
            raise Exception('Overflow')
        self.__stack.append(value)

    def pop(self):
        if self.is_empty():
            raise Exception('Underflow')
        return self.__stack.pop()

    def top(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.__stack[-1]


# Khởi tạo stack với capacity là 4
my_stack = MyStack(4)
# Kiểm tra stack có rỗng không
print(my_stack.is_empty())  # True

# Thêm phần tử vào stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

# Kiểm tra stack đã đầy chưa
print(my_stack.is_full())  # True

# Thử thêm phần tử vào stack khi đã đầy
try:
    my_stack.push(5)
except Exception as e:
    print(e)  # Overflow

# Kiểm tra phần tử trên cùng của stack
print(my_stack.top())  # 4

# Loại bỏ phần tử từ stack
print(my_stack.pop())  # 4
# Kiểm tra lại stack có đầy không
print(my_stack.is_full())  # False

# Kiểm tra lại stack có rỗng không
print(my_stack.is_empty())  # False

# Kiểm tra phần tử trên cùng của stack
print(my_stack.top())  # 3
