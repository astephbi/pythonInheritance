class Car:
    brand = ""
    model= ""
    year = 0
    speed=0

#inheritance is added by writing the parent in brackets
class Electricity(Car): 
    battery_capacity = 0
class CEngineCar(Car):
    engine_capacity = 0

electric_car = Electricity()
electric_car.battery_capacity = 2000 

car = Car()
car.year = 13

print(f"")