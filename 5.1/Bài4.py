class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Phương tiện: {self.brand} {self.model} (Sản xuất: {self.year})")
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):

        super().display_info()

        print(f" -> Thuộc loại: Ô tô | Số cửa: {self.num_doors}")


class Bike(Vehicle):
    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model, year)
        self.bike_type = bike_type

    def display_info(self):
  
        super().display_info()
 
        print(f" -> Thuộc loại: Xe đạp/Mô tô | Kiểu dáng: {self.bike_type}")


if __name__ == "__main__":
    print("--- QUẢN LÝ PHƯƠNG TIỆN ---")
    

    my_car = Car(brand="Toyota", model="Camry", year=2023, num_doors=4)
    my_car.display_info()
    
    print("-" * 30)

    my_bike = Bike(brand="Trek", model="Marlin 7", year=2022, bike_type="Mountain Bike")
    my_bike.display_info()
    
    print("-" * 30)
    
    my_motorcycle = Bike(brand="Honda", model="SH150i", year=2024, bike_type="Scooter")
    my_motorcycle.display_info()