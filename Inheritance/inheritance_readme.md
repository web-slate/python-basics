## Inheritance

- Inheritance allows us to define a class that inherits all features and methods from the another class

- Parent Class or base class: Parent class is the class being inherited from
- Pass keyword when you do not want to add any other properties or methods to the class

class Student(Person):
   pass

Add /_/_init__() Function

The __init__() function is called automatically every time the class is being used to create a new object.

When you add the __init__() function, the child class no longer inherit the parent's /_/_init__() function

The child's __init__() function overrides the inheritence of the parent's __init__() function

To keep the inheritence of the parent's /_/_init__(), add a call to the parent's /_/_init__()

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

## Super()

Super() function that will make the child class inherit all the methods and properties from its parent.

super().__init__()

If you add a method in the child class with thhe same name as a function in the parent class, the inheritance of the parent method will be overridden.

def myfunc():
  x = 300
  print(x)

myfunc()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

def myfunc():
  global x
  x = 300

myfunc()

print(x)