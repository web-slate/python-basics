from stylepy import h1, h2, h3, h4, h5, h6

h1('\n >>>> Operators Example')
print('Arithmetic operators: (+,-,*,/,//,%,**)')
print('Assignment operators: (=,+=,-=,*=,/=,//=,**=,\=,^=,>>=,<<=)')
print('Comparison operators: (==,!=,>,>=,<,<=)')
print('Logical operators: (and ,or ,not)')
print('Membership operators: (in ,not in)')
print('Identity operators: (is, is not)')
print('Bitwise Operators: (&,|,^,~,<<,>>)')

h2('\n Arithmetic Interesting Operators')
h3 (' >>> Exponentiation Operator')
x = 2
y = 5
print('when x is 2 and y = 5')
print('Exponentiation: x ** y is 2 to power of 5 aka 2^5 = ', x**y)

h4 ('\n >>> Floor Division Operator')
fruits = 10
share_people = 3
h5('when fruits are 10 and people are 3 and we need to share the fruits')
h6('then we can use Floor Division ')
print('Maximum can be shared: fruits // share_people = ', fruits // share_people)