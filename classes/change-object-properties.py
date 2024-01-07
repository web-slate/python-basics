import simple_class as sc

# Without creating an object or instance we cannot work/use the class
# An object is a memory it has all the features and functions that defined in the class

# create an object
def get_length1(bus):
    return bus.length

bus = sc.Bus()
print(f"Bus length : {bus.length}")
bus.length = 10
bus.get_length = get_length1
print(f"Bus length : {bus.length}")
print(f"bus length is : {bus.get_length(bus)}")
bus.additional_param = 9

# we can assign and change the properties from out side but it is a bad design


print(f" bus additional param : {bus.additional_param}")

apple = sc.Fruit()

washing_machine = sc.washingMachine()