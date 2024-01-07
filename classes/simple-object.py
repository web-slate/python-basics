# import simple_class as sc
from simple_class import Bus, Fruit, WashingMachine

bus = Bus()
print(f"Bus lenghth is {bus.model}")

fruit = Fruit()
print(f"Fruit name : {fruit.name}, color: {fruit.color} ")

wash_machine = WashingMachine()

wash_machine.wash_clothes()
print(f"Washing Machine name : {wash_machine.brand}, color: {wash_machine.model} ")


