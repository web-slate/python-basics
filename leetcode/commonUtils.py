def timeComplexity(value, desc):
    result = f'\n 🕒 Time Complexity: Approximately {value}'

    if (desc):
        result += f'\n     Description: {desc}'
    print(result)

def spaceComplexity(value, desc):
    result = f' 💾 Space Complexity: Approximately {value}'

    if (desc):
        result += f'\n     Description: {desc}'
    print(result)
