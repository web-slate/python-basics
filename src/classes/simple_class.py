# Blue prints or skelentons for entities
# Python keyword for the class is "class"
from stylepy import h1,h2,h3
class Fruit:
    name = "Apple"
    color = "red"

class WashingMachine:
    color = "white"
    model = "1A"
    brand = "IFB"
    capacity = 7
    price = 999.0
    water_consumption = 2.5

    def wash_clothes(self):
        h3("washing initiated")

class Bus:
    length=0
    brand = "Volvo"
    model = "V9"
    capacity = 50
    fuel_type = "Diesel"
    price = 250000

def get_length():
        return Bus.length



        


