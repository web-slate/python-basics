## Class 

A class should have a properties and methods.

- Properties are like features

- Methods are its behaviour or functionalities

- Class is a back bone of OOP

keyword: class

Class is a blue print or skeleton -> assume like there is no physical form

## Instance or Object

Instances should be created to make use of class

class MyClass:
    x=5

instance_1 = MyClass()
instance_2 = MyClass()


## class built in functions:

### \_\_init__()
Built in \_\_init__() Function

What you want to create when you are creating an object -> All should present inside an \_\_init__() function
 -> Assign values to its  properties
 -> Operations that are necessary to do when the object is created

### \_\_str__()
 \_\_str__() Function

  It returns how the object can be represented as a string
  We can override this by our own

## Methods
 Behaviour or action:

 Methods:
 -> In one line these are object functions, what are all the functions that object can do or it poses

## Self

 The self parameter is a refrence to the current instance of the class, 
 Used to access variables that belongs to the class

 It doesn't have to be named self, we can call it whatever you like

 It should be the first parameter to any function in the class

## Delete
 Delete the properties of the object

 del p.height

 Delete objects as well

## pass

 pass:
 class definitions cannot be empty
 using pass we can make the content of the class functions can be empty.

## Class Internals:

 Programmers can create modular, reusable code that models or represents real-world entities or concepts in an intutive way.
 Classes form the backbone object oriented programmingand facilitate the principles of encapsultion, inheritance and polymorphism

 Internals of the class:

 1. Defining a class: First, you define a class using the 'class' keyword.  Python executes the class block, which may contain method definitions, class variables, and other statements

 2. NameSpace creation: Python creates a namespace where all its attributes and methods are stored.
 3. Class Object Creation: Once the class definition is complete, Python creates a class object and assign it to the name provided after the class, that class allows for object creation
 class Creation: First, you define a class using the 'class' keyword. Python



