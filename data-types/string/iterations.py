print('\n >>>> String Iteration Example')

greet = 'welcome'

print('\n >>>> Iterate using for loop')
# for word in greet:
#     print(word)

print('\n >>>> Iterate using while loop')
index = 0
while index < len(greet):
    print(greet[index])
    index += 1