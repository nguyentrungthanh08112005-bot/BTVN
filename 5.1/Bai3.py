class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Tôi tên là {self.name}, {self.age} tuổi.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        
        self.student_id = student_id

    def study(self):
        print(f"Sinh viên {self.name} (Mã SV: {self.student_id}) đang học bài...")

if __name__ == "__main__":

    sv1 = Student(name="Nguyễn Văn A", age=20, student_id="SV2026_001")

    print("--- Thông tin sinh viên ---")
    print(f"Tên: {sv1.name}")
    print(f"Tuổi: {sv1.age}")
    print(f"Mã sinh viên: {sv1.student_id}")
    print("-" * 25)

    sv1.introduce()

    sv1.study()