from collections import namedtuple
from dataclasses import dataclass

# 以前简单的类可以使用 namedtuple 实现。
Car = namedtuple('Car', 'color mileage name')

my_car = Car('red', 3812.4, "Auto")
print(my_car.color)
print(my_car.name)


# 方法二：使用dataclass
@dataclass
class Car:
    color: str
    mileage: float


my_car = Car('red', 3812.4)
print(my_car.color)
print(my_car)
