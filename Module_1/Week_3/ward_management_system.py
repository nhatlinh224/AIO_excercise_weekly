from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass

    def get_yob(self):
        return self._yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")


# Tạo đối tượng Student, Doctor và Teacher
student1 = Student("John Doe", 2010, 7)
doctor1 = Doctor("Dr. Smith", 1988, "Cardiology")
teacher1 = Teacher("Mrs. Johnson", 1975, "Mathematics")

# Gọi phương thức describe để hiển thị thông tin
student1.describe()
doctor1.describe()
teacher1.describe()


class Ward:
    def __init__(self, name):
        self._name = name
        self._list_people = list()

    def add_person(self, person: Person):
        self._list_people.append(person)

    def describe(self):
        print(f"Ward: {self._name}")
        for p in self._list_people:
            p.describe()

    def count_doctor(self):
        counter = 0
        for p in self._list_people:
            if isinstance(p, Doctor):
                counter += 1
        return counter

    def sort_yob(self):
        return self._list_people.sort(key=lambda x: x.get_yob(), reverse=True)

    def compute_average(self):
        counter = 0
        total = 0
        count = len(self._list_people)
        if count == 0:
            return 0  # Tránh chia cho 0 khi danh sách trống
        for p in self._list_people:
            if isinstance(p, Teacher):
                counter += 1
                total += p.get_yob()
        return total / counter if counter > 0 else 0  # Trả về giá trị trung bình


# Tạo Ward và thêm các đối tượng vào
ward1 = Ward('Ward1')
ward1.add_person(student1)
ward1.add_person(doctor1)
ward1.add_person(teacher1)

# Gọi phương thức describe để hiển thị thông tin
ward1.describe()

# Sắp xếp theo năm sinh và hiển thị lại
ward1.sort_yob()
ward1.describe()

# Đếm số lượng doctor
print(f"Number of doctors: {ward1.count_doctor()}")

# Tính giá trị trung bình năm sinh của các giáo viên
print(f"Average year of birth (teachers): {ward1.compute_average()}")
