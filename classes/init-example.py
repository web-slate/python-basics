from stylepy import h1, h2, h3, h4, h5, h6
# __init__() is a built function
# https://chat.openai.com/share/eb3388df-6669-41ee-a16e-d471ec115799
# It facilitates the initial creation of object properties and do the initial function calls 
# TypeError: Bus.__init__() takes 0 positional arguments but 1 was given
class Bus:

    # Below one gives this error # TypeError: Bus.__init__() takes 0 positional arguments but 1 was given 
    # def __init__():
    #     length = 4
    #     width = 2

    # What the above error means, The error you're encountering typically occurs when __init__() method is defined without any parameters,
    # But, python tries to call it with the "self" argument automatically


    def __init__(self):
    
        self.length = 4
        self.width = 2
    # def __str__(self):
    #     # print(f"length is {self.length}")
    #     # return f"length is {self.length}"

    # If the methods are not defined with a first parameter then we cannot use the object variables, to access 
    # To access object variables

    # def area():
    #     length = 4
    #     width = 2
    #     return length*width
    # def area(self):

    #     return self.length*self.width
    

bus = Bus()
print(bus)
# bus.length
# print(bus.area())
print(f"Bus object has created")

    