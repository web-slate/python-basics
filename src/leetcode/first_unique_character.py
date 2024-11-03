from stylepy import h1,h2,h3,h4,h5,h6
from collections import Counter

def first_uniq_char_brute1(s: str) -> int:
  count_char = {i: s.count(s[i])  for i in range(len(s))  }
  for index, count  in count_char.items():
    if count == 1:
      return index
  return -1

def first_uniq_char_brute2(s: str) -> int:
  count_char = Counter(s) 
  stack = {}
  for i in range(len(s)):
    if s[i] not in stack: 
      stack[s[i]] = i
  char = next((char for char, count  in count_char.items() if count == 1), -1 )
  return stack[char] if char in stack  else -1 

def first_uniq_char_optimised(s: str) -> int:
    result = next((i for i in range(len(s)) if s.count(s[i])==1), -1 )
    return result

def first_uniq_char_optimised2(s: str) -> int:
    for i in range(len(s)):
       if s.count(s[i]) == 1:
          return i
    return -1

h1("Brute-force 1")
s = 'leetcode'
index = first_uniq_char_brute1(s)
h3(f"first non repeating character index {index} for {s} ")

s = 'loveleetcode'
index = first_uniq_char_brute1(s)
h3(f"first non repeating character index {index} for {s} ")

s = 'aabb'
index = first_uniq_char_brute1(s)
h3(f"first non repeating character index {index} for {s} ")

h1("Brute-force 2")
s = 'leetcode'
index = first_uniq_char_brute2(s)
h3(f"first non repeating character index {index} for {s} ")

s = 'loveleetcode'
index = first_uniq_char_brute2(s)
h3(f"first non repeating character index {index} for {s} ")

s = 'aabb'
index = first_uniq_char_brute2(s)
h3(f"first non repeating character index {index} for {s} ")


h1("Optimised")
s = 'leetcode'
index = first_uniq_char_optimised(s)
h3(f"first non repeating character index {index} for {s} ")

s = 'loveleetcode'
index = first_uniq_char_optimised(s)
h3(f"first non repeating character index {index} for {s} ")

s = 'aabb'
index = first_uniq_char_optimised(s)
h3(f"first non repeating character index {index} for {s} ")


h1("Optimised 2 ")
s = 'leetcode'
index = first_uniq_char_optimised2(s)
h3(f"first non repeating character index {index} for {s} ")

s = 'loveleetcode'
index = first_uniq_char_optimised2(s)
h3(f"first non repeating character index {index} for {s} ")

s = 'aabb'
index = first_uniq_char_optimised2(s)
h3(f"first non repeating character index {index} for {s} ")