from stylepy import h1,h4,h2,h3
h1('\n >>>> Split String Example');

original = "Hello, World!"
target = original.split(",")
print("Using Native Split function: ", target)

# Faced `TabError: inconsistent use of tabs and spaces in indentation`

def splitString(text, sepearator):
  word = ''
  splitted_list = []
  
  for char in text:
    if char == sepearator:
        splitted_list.append(word)
        word = ''
    else:
        word += char
  
  if word != '':
      splitted_list.append(word)

  return splitted_list

h4('Using Custom function: ', splitString(original, ','))
h4('Custom Def Time and Space Complexity is O(n)')