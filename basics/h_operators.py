from stylepy import h1, h2, h3, h4, h5, h6

h1('\n >>>> Operators Example')
h5('Arithmetic operators: (+,-,*,/,//,%,**)')
h5('Assignment operators: (=,+=,-=,*=,/=,//=,**=,\=,^=,>>=,<<=)')
h5('Comparison operators: (==,!=,>,>=,<,<=)')
h5('Logical operators: (and ,or ,not)')
h5('Membership operators: (in ,not in)')
h5('Identity operators: (is, is not)')
h5('Bitwise Operators: (&,|,^,~,<<,>>)')

h2('\n Arithmetic Interesting Operators')
h3 (' >>> Exponentiation Operator')
x = 2
y = 5
h4('when x is 2 and y = 5')
h5('Exponentiation: x ** y is 2 to power of 5 aka 2^5 = ', x**y)

h4 ('\n >>> Floor Division Operator')
fruits = 10
share_people = 3
h4('when fruits are 10 and people are 3 and we need to share the fruits')
h5('then we can use Floor Division ')
h6('Maximum can be shared: fruits // share_people = ', fruits // share_people)