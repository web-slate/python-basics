def returning_one():
  return 1

def returning_one_with_comma():
  return 1,

def returning_one_two_three():
  return 1,2,3

print(type(returning_one()), 'returning_one: ', returning_one())
print(type(returning_one_with_comma()), 'returning_one_with_comma: ', returning_one_with_comma())
print(type(returning_one_two_three()), 'returning_one_two_three: ', returning_one_two_three())