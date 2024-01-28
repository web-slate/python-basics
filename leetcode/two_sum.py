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
  
  print(type(dicti), dicti)
  for i in range(len(lst)):
    complement = target - lst[i] 
    if complement in dicti and dicti[complement] != i:
      return [i, dicti[complement]]
  
print("""Brute-force solution""")
print(f"list[2,5,7,4] and target 11 {brute_force([2,5,7,4], 11 )}")
print(f"list[2,5,7,4] and target 11 {time_optimized([2,5,7,4], 11 )}")