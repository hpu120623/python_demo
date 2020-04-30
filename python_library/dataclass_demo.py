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

print('-'*20)

my_car = Car('red', 3812.4)
print(my_car.color)
print(my_car)

print('='*20)

@dataclass
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

test = InventoryItem('python', 20.2, 2)
print(test.total_cost())