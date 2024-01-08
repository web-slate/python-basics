class Parent:
    parent_name1 = "Sivan"
    def __init__(self, name=""):
        print(" Parent class is created")
        self.parent_name = "Sivan"
    def get_parent_name(self):
        print(f" Parent Name is {self.parent_name}")

    def grace_us(self):
        print(" All is well")

    
class Child(Parent):
    def __init__(self, name, parent_name=""):
        # Parent.__init__(self, name=parent_name)
        super().__init__(name=parent_name)

        # print(" Overriding Parent's Init class")
        self.name = name
        print(" Child Name is Vinayagar")
        

# child_class = Child(name= "Vinayagar")
# # print(" Trying to call parent init")
# print(child_class.parent_name)
        
child_class = Child("Vinayagar", "Sivan")
print(" Trying to call parent init")
child_class.get_parent_name()



print(" To use global variable inside a function we need use a keyword : Global")

x = 5

print("Initial glbal varibale value is x : " , x)
def myfunc():
    global x
    x = 300
    print("Set the global variable x inside a function ", x)
    def myfunc2():

        x = 100
        print("second Local variable is", x)
    myfunc2()
  
myfunc()
print("global variable is x ", x)

