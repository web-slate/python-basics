from stylepy import h1, h2, h3, h4, h5, h6

# Statement
h1('\n >>>> Statement Example')

# isEligibleToVote Function
h2('\n >>>> isEligibleToVote Function with passing age')

def isEligibleToVote(age: int = 0) -> None:
    try:
      if(age > 0 and age < 21):
          print(str(age) + ' Wow, You will be soon eligible to vote')
      elif(age > 21):
          print(str(age) + ' Congrats, You are eligible to vote!')
      else:
          print(str(age) + ' Invalid `age` parameter')
    except Exception as e:
      print('Got error for param "' + age + '"\nError is ', e)

# Example usage
h3('\n >>>> Passing nothing consider default parameter if provided')
isEligibleToVote()
h4('\n >>>> Passing `16` return "Wow, You will be soon eligible to vote"')
isEligibleToVote(16)
h5('\n >>>> Passing `19` return "Wow, You will be soon eligible to vote"')
isEligibleToVote(19)  
h6('\n >>>> Passing `25` return "Congrats, You are eligible to vote!"')
isEligibleToVote(25)  
print('\n >>>> Passing `\'\'` as parameter throws TypeError: \'<\' not supported between instances of \'str\' and \'int\'')
isEligibleToVote('')