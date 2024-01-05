#Square number without lambda
def sum(a ):
  return a**2

numbers = list(range(1, 6, 1 ))
squared = list(map(sum, numbers))
print("Numbers: ", numbers,)
print("Squared Numbers", squared)


#Square number with lambda
numbers = list(range(1,6,1))
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers", squared)

