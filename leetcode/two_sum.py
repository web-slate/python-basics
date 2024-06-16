from stylepy import h1,h2,h3,h4,h5,h6
import numbers

def brute_force(lst, target):
  if type(target) != int : 
    return 0
  for i in range(len(lst)): 
    for j in range(len(lst)):
      if lst[i] + lst[j] == target: 
        return [i, j ]

def time_optimized(lst, target):
  if not isinstance(target, numbers.Number):
    return 0
  dicti = {}
  for index, value in enumerate(lst):
    dicti[value] = index
  
  h3(type(dicti), dicti)
  for i in range(len(lst)):
    complement = target - lst[i] 
    if complement in dicti and dicti[complement] != i:
      return [i, dicti[complement]]
  
h1("""Brute-force solution""")
h3(f"list[2,5,7,4] and target 11 {brute_force([2,5,7,4], 11 )}")
h3(f"list[2,5,7,4] and target 11 {time_optimized([2,5,7,4], 11 )}")