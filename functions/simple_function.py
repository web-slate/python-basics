
from stylepy import h4
def returning_one():
  return 1

def returning_one_with_comma():
  return 1,

def returning_one_two_three():
  return 1,2,3

h4(type(returning_one()), 'returning_one: ', returning_one())
h4(type(returning_one_with_comma()), 'returning_one_with_comma: ', returning_one_with_comma())
h4(type(returning_one_two_three()), 'returning_one_two_three: ', returning_one_two_three())