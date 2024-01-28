class ValidParenthesis:
  def is_valid(self, x: str ):
    stack = []
    parenthesis = {'[' : ']', '(' : ')', '{' : '}'}
    for char in x:
      if char in parenthesis:
        stack.append(parenthesis[char])
      elif not stack or stack.pop() != char:
        return False
    return not stack
a = ValidParenthesis()
string_value = '()[(]'
print(f"given string {string_value} is { 'valid ' if a.is_valid(string_value) else 'not valid '} paranthesis")
