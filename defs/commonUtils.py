from stylepy import timeComplexity
from stylepy import spaceComplexity
from stylepy import h1,h2,h3,h4,h5,h5,h6
def timeComplexity(value, desc):
    result = f'\n 🕒 Time Complexity: Approximately {value}'

    if (desc):
        result += f'\n    Description: {desc}'
    h4(result)
timeComplexity("value","desc")
def spaceComplexity(value, desc):
    result = f' 💾 Space Complexity: Approximately {value}'

    if (desc):
        result += f'\n    Description: {desc}'
    h4(result)
spaceComplexity("value","desc")