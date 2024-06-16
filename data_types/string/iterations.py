from stylepy import h1,h2,h3
h1('\n >>>> String Iteration Example')

greet = 'welcome'

h3('\n >>>> Iterate using for loop')
for word in greet:
    print(word)

h3('\n >>>> Iterate using while loop')
index = 0
while index < len(greet):
    print(greet[index])
    index += 1
