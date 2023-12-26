print('\n >>>> Float Iteration Example')

mark = 78.80
weight = 68.50
height = 6.3
distance = 10.2
price = 27.50

# for i in range(1,11): 
    # print(i)

# i = 1
# while i < 11:
#     print(i)
#     i +=1
    
# i = 10
# while i > 0:
#     print(i)
#     i-=1

print('\n >>>> Iterate using for loop with type casting')
print(' >>>> Follow this approach on demand and Its not recommended')
for text in str(mark):
    print(text)

print('\n >>>> Iterate using for loop with operators')
start = 0.0
end = mark
step = 0.1

current_value = start
while current_value <= end:
    print(current_value)
    current_value += step

# print('\n >>>> Iterate using for loop with range')
# start = 0.0
# end = mark
# step = 0.1

# for i in range(int((end-start) / step) + 1):