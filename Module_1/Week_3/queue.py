class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if self.is_full():
            raise Exception('Queue is full')
        self.__queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.__queue[0]


# Kiểm tra lớp MyQueue với ví dụ trong đề bài
queue1 = MyQueue(capacity=5)

queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())  # False

print(queue1.front())  # 1

print(queue1.dequeue())  # 1

print(queue1.front())  # 2

print(queue1.dequeue())  # 2

print(queue1.is_empty())  # True
