import simple_class as sc
from stylepy import h1, h2, h3, h4, h5, h6

# Without creating an object or instance we cannot work/use the class
# An object is a memory it has all the features and functions that defined in the class

# create an object
def get_length1(bus):
    return bus.length

bus = sc.Bus()
h1(f"Bus length : {bus.length}")
bus.length = 10
bus.get_length = get_length1
h2(f"Bus length : {bus.length}")
h3(f"bus length is : {bus.get_length(bus)}")
bus.additional_param = 9

# we can assign and change the properties from out side but it is a bad design


h4(f" bus additional param : {bus.additional_param}")

apple = sc.Fruit()

washing_machine = sc.WashingMachine()