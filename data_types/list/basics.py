import data_types.commonUtils as utils

utils.print_h1('List Basics')

utils.print_ordered_list([
    'List is Ordered (order will not be changed)',
    'List is Changable'
])

fruits = ['apple', 'orange', 'cherry']
print('\nCreated fruits list: ', fruits)
print('Access Apple: fruits[0]: ', fruits[0])
print('Adding New Fruit: Grape')
fruits.append('grapes')
print('Picking Last item from fruit:', fruits[-1])

print('Iterating the Fruits')
for fruit in fruits:
    print(' - ', fruit)

marks = [78, 90, 75, 61, 90]
print('\nCreated marks list: ', marks);
marks.reverse()
print('Reversed the Marks using reverse(): ', marks);
marks.sort()
print('Sort the Marks in ascending using sort(): ', marks);
marks.sort(reverse=True)
print('Sort the Marks in descending using sort(reverse=True): ', marks);
print('marks : ', marks)

conf = [True, False]
print('conf =: ', conf)

employee = ['Venkat', 37, 'Developer']
print('employ: ', employee)


'''
1. How iterator internally working?
2. When do we go for list
3. How memory allocation working in List data type?
4. Which data structure can be created using List?
'''
