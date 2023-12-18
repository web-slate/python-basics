print('\n >>>> Split String Example');

original = "Hello, World!"
target = original.split(",")
print("Using Native Split function: ", target)


def splitString(text, sepearator):
  word = ''
  splitted_list = []
  
  for i in text:
    if i == sepearator:
        splitted_list.append(word)
        word = ''
    else:
        word += i
  
  if word != '':
      splitted_list.append(word)

  return splitted_list

print('Using Custom function: ', splitString(original, ','))
print('Custom Def Time and Space Complexity is O(n)')