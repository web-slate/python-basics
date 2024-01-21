text = """
Array is a collection of emlements. List is a array in python.
For advanced array we can use numpy library

"""

#slice
list1 = [10, 20, 30, 40]
list2 = list1[1:3]
print("list1 ", list1)
print("list2 ", list2 )

print("if I want to include last time then how? ")
list3 = list1[2:]
print("list 3 with last time. starting with 2nd index[2:]", list3)

#copy the list
text = """
In Python, when you assign one list to another using = (as in list3 = list1), 
you are creating a reference to the same list object, not a new copy of the list.

"""
print(text)

list3 = list1
print("assign list3 = list1 and print list3 ")
print("list3", list3)

print("Amend the first index value for the list3 and print list1 and list3")
list3[0] = 1

print("list1 ", list1 )
print("list3 ", list3 )

text = """
Shallow Copy:
A shallow copy creates a new object but does not create new objects 
for the elements within the original object. It means that 
the new object is a copy of the original one, 
but the elements inside the objects still refer to the same objects.

You can use the copy() method or the [:] slicing syntax 
to create a shallow copy of a list:
"""

print(text)

original_list = [1, 2, 3, 4, 5]
# Using copy() method
shallow_copy_1 = original_list.copy()
# Using slicing syntax
shallow_copy_2 = original_list[:]
# Assign to another list
shallow_copy_3 = original_list

# Modifying the original list
original_list[0] = 10
print("Original list", original_list)      # Output: [10, 2, 3, 4, 5]
print("Shallow copy 1", shallow_copy_1)    # Output: [1, 2, 3, 4, 5]
print("Shallow copy 2", shallow_copy_2)    # Output: [1, 2, 3, 4, 5]
print("Shallow copy 3", shallow_copy_3)    # Output: [10, 2, 3, 4, 5]

del shallow_copy_3[0]
print("Original list after deleting shallow copy 3 ", original_list)
print("shallow_copy_1 list after deleting shallow copy 3 ", shallow_copy_1)
print("shallow_copy_2 list after deleting shallow copy 3 ", shallow_copy_2)

print("The key concept is whether the elements inside the list are mutable or immutable.")
text = """
When you create a shallow copy of a list containing immutable objects, 
modifying the original list's elements won't affect the shallow copy,
 because the values of those elements cannot be changed
"""

print(text)

original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
shallow_copy = original_list.copy()
# Modifying an element inside the list
original_list[0][0] = 10

print("original list", original_list)  # Output: [[10, 2, 3], [4, 5, 6], [7, 8, 9]]
print("shallow_copy", shallow_copy)   # Output: [[10, 2, 3], [4, 5, 6], [7, 8, 9]]

text = """
What is shallow? 

shallow copy of a data structure like a list,
you are creating a new structure that has the same outermost elements 
as the original, but it doesn't recursively duplicate the elements inside 
the structure. The depth of the copy is limited, and modifications 
to the inner elements are shared between the original and the shallow copy
"""

print(text)

list1 = [10, 20 ,30 , 40 ]




text = """
1. len(): Returns the number of elements in a list.

2. max() and min(): Return the maximum and minimum values in a list, respectively.

3. sum(): Returns the sum of all elements in a list.

4. sorted(): Returns a new sorted list from the elements of the given iterable.

5. list(): Converts an iterable (e.g., tuple, string, or another list) into a list.

6. append(): Adds an element to the end of a list.

7. extend(): Extends a list by appending elements from an iterable.

8. insert(): Inserts an element at a specified position in a list.

9. remove(): Removes the first occurrence of a specified value.

10. pop(): Removes and returns the element at the specified index (default is the last element).

11. index(): Returns the index of the first occurrence of a specified value in a list.

12. count(): Returns the number of occurrences of a specified value in a list.

13. reverse(): Reverses the order of elements in a list (in-place).

14. copy(): Creates a shallow copy of a list.

15. clear(): Removes all elements from a list.

16. join(): Concatenates a list of strings into a single string using a specified delimiter.

17. slice(): Returns a portion of a list using slicing.

"""

print(text)