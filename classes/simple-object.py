# import simple_class as sc
from simple_class import Bus, Fruit, WashingMachine
from stylepy import h1,h2,h3,h4,h5,h6
bus = Bus()
h2(f"Bus lenghth is {bus.model}")

fruit = Fruit()
h3(f"Fruit name : {fruit.name}, color: {fruit.color} ")

wash_machine = WashingMachine()

wash_machine.wash_clothes()
h4(f"Washing Machine name : {wash_machine.brand}, color: {wash_machine.model} ")


