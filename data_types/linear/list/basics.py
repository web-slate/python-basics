import data_types.commonUtils as utils
from stylepy import h1,h2,h3,h4,h5
utils.print_h1('List Basics')

utils.print_ordered_list([
    'List is Ordered (order will not be changed)',
    'List is Changable'
])

fruits = ['apple', 'orange', 'cherry']
h1('\nCreated fruits list: ', fruits)
h2('Access Apple: fruits[0]: ', fruits[0])
h3('Adding New Fruit: Grape')
fruits.append('grapes')
h3('Picking Last item from fruit:', fruits[-1])

h4('Iterating the Fruits')
for fruit in fruits:
    print(' - ', fruit)

marks = [78, 90, 75, 61, 90]
h1('\nCreated marks list: ', marks);
marks.reverse()
h4('Reversed the Marks using reverse(): ', marks);
marks.sort()
h4('Sort the Marks in ascending using sort(): ', marks);
marks.sort(reverse=True)
h4('Sort the Marks in descending using sort(reverse=True): ', marks);
h4('marks : ', marks)

conf = [True, False]
h3('conf =: ', conf)

employee = ['Venkat', 37, 'Developer']
h4('employ: ', employee)


'''
1. How iterator internally working?
2. When do we go for list
3. How memory allocation working in List data type?
4. Which data structure can be created using List?
'''
