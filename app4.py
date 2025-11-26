
class Vehicle:
    def __init__(self, mileage, battery_capacity):
        self.mileage = mileage
        self.battery_capacity = battery_capacity

    def show_mileage(self):
        print(f"Vehicle mileage: {self.mileage} km/hr")

    def show_battery_capacity(self):
        print(f"Vehicle battery capacity: {self.battery_capacity} kWh")



class Car(Vehicle):
    def __init__(self, mileage, battery_capacity, brand):
        super().__init__(mileage, battery_capacity)
        self.brand = brand

    
    def show_mileage(self):
        print(f"{self.brand} Car mileage: {self.mileage} km/hr")

   
    def show_battery_capacity(self):
        print(f"{self.brand} Car battery capacity: {self.battery_capacity} kWh")



class ElectricCar(Vehicle):
    def __init__(self, mileage, battery_capacity, model):
        super().__init__(mileage, battery_capacity)
        self.model = model

   
    def show_mileage(self):
        print(f"Electric Car ({self.model}) mileage: {self.mileage} km/hr")

    
    def show_battery_capacity(self):
        print(f"Electric Car ({self.model}) battery capacity: {self.battery_capacity} kWh")




v = Vehicle(50, 40)
v.show_mileage()             
v.show_battery_capacity()   

c = Car(60, 50, "Toyota")
c.show_mileage()            
c.show_battery_capacity()    

e = ElectricCar(120, 100, "Tesla Model S")
e.show_mileage()             
e.show_battery_capacity()    
