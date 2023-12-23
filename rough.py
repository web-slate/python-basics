# table = [0] * (7)
# print(table)

# def using_front_and_back(word):
#     mid_point = len(word) // 2 # 5
#     last_index = len(word) # 9

#     mid_index = mid_point -1
#     first_part = ''
#     second_part = ''
#     for rest_index in range(last_index - 1, mid_point - 1, -1):
#         # print(f'i: {mid_index} {word[mid_index]} and j: {rest_index} {word[rest_index]}')
#         first_part += word[rest_index]
#         second_part += word[mid_index]
#         mid_index -= 1
        
#     return first_part + second_part

# print(using_front_and_back('EVIL OLIVE'))
# print(using_front_and_back('RISE SIR'))

# def is_palindrome():
#     start = 0
#     end = 9
#     word = 'EVIL OLIVE'

#     while start < end:
#         if word[start] != word[end]:
#             return False

#         start +=1
#         end -=1
    
    
        # print('start: ', start, word[start], ' end: ', end, word[end]);

def is_palindrome(s):
    s = s.lower()  # Convert to lower case, but keep spaces
    start, end = 0, len(s) - 1

    while start < end:
        # Skip spaces in the start pointer
        while start < end and s[start] == " ":
            start += 1

        # Skip spaces in the end pointer
        while end > start and s[end] == " ":
            end -= 1

        # Compare characters
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True

phrases = ["EVIL OLIVE", "TACO CAT", "HUH", "DO GEESE SEE GOD", "BORE ME ROB", "RISE SIR", "MADAM", "DIVE VID"]
results = {phrase: is_palindrome(phrase) for phrase in phrases}

print(results)



'''
Decrement Iteration (9-5)
Additional Index (4-0)

20 - 19
 10

19-10 = 9
10 -1 = 9, 0
===
9-0
'''

