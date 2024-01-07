def timeComplexity(value, desc):
    result = f'\n 🕒 Time Complexity: Approximately {value}'

    if (desc):
        result += f'\n    Description: {desc}'
    print(result)

def spaceComplexity(value, desc):
    result = f' 💾 Space Complexity: Approximately {value}'

    if (desc):
        result += f'\n    Description: {desc}'
    print(result)

def print_h1(text):
    print(f"\n{'=' * 40}\n{text}\n{'=' * 40}")

def print_h2(text):
    print(f"\n{'-' * 35}\n{text}\n{'-' * 35}")

def print_h3(text):
    print(f"\n{text}\n{'-' * 30}")

def print_h4(text):
    print(f"\n{text}\n{'-' * 25}")

def print_h5(text):
    print(f"\n{text}\n{'-' * 20}")

def print_h6(text):
    print(f"\n{text}\n{'-' * 15}")

def print_ordered_list(items):
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

def print_bullet_list(items, bullet_char='*'):
    for item in items:
        print(f"{bullet_char} {item}")
