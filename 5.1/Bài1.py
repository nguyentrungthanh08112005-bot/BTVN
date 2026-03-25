class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Tên sách: {self.title}")
        print(f"Tác giả: {self.author}")
        print(f"Năm xuất bản: {self.year}")
        print("-" * 20)

# 3. Tạo ít nhất 2 đối tượng Book và hiển thị thông tin
book1 = Book("Đắc Nhân Tâm", "Dale Carnegie", 1936)
book2 = Book("Số Đỏ", "Vũ Trọng Phụng", 1936)

book1.display_info()
book2.display_info()