class Car:
    brand = ""
    model= ""
    year = 0
    speed=0

    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


#inheritance is added by writing the parent in brackets
class Electricity(Car): 
    battery_capacity = 0
    def __init__(self, brand: str, model:str, year:int):
        super().__init__(brand, model, year)
        self.battery_capacity
class CEngineCar(Car):
    engine_capacity = 0

electric_car = Electricity()
electric_car.battery_capacity = 2000 

car = Car()
car.year = 13
