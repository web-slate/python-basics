a = "Hello, World!"
b = a.split(",")
print("Using Split function: ", b)


def splitString(text, sepearator):
  word = ''
  list_ = []
  
  for i in text:
    if i == sepearator:
        list_.append(word)
        word = ''
    else:
        word += i
  
  if word != '':
      list_.append(word)

  return list_

print('Using Custom function: ', splitString('Hello, World!', ','));
print('Custom Def Time and Space Complexity is O(n)')