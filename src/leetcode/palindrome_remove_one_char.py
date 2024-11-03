
def valid_palindrome(s):

  def is_valid(i, j ):
    while i < j: 
      if s[i] != s[j]:
        return False
      else:
        i += 1
        j -= 1
    return True
  def remove_one_from_range(i, j ):
    return is_valid(i+1, j) or is_valid(i, j-1 )

  left, right = 0 , len(s) -1 
  while left < right:
    if s[left] != s[right]:
      return remove_one_from_range(left, right )
    else:
      left += 1
      right -= 1
  return True

s = 'aba'
print(f" {s} is {'palindrome' if valid_palindrome(s) else 'not a palindrome'} ")
s = 'abac'
print(f" {s} is {'palindrome' if valid_palindrome(s) else 'not a palindrome'} ")
s = 'abacd'
print(f" {s} is {'palindrome' if valid_palindrome(s) else 'not a palindrome'} ")