from stylepy import h3,h2,h4
def print_even_sequence(array):
  for a in array:
    if a % 2 == 0:
      print("\nSequence for {0}".format(a))
      for k in range(0,a):
        print(k, end=" ")
        
print_even_sequence([10, 22, 33, 44, 55, 66, 77])
h2('\n Here O(a * k) , where a = size of array and k is largest even')

h3('\n\n 🕒 Time Complexity: Approximately O(n × m) \n In the worst case, where n is the length of the array and m is the average size of the even numbers. However, the actual time complexity can vary significantly based on the contents of the input array.')
h3('\n 💾 Space Complexity: O(1) \n As it only uses a constant amount of additional memory.')