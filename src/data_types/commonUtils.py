import pprint
from stylepy import timeComplexity
from stylepy import spaceComplexity
from stylepy import h1,h2,h3,h4,h5,h5,h6
def timeComplexity(value, desc):
    result = f'\n 🕒 Time Complexity: Approximately {value}'

    if (desc):
        result += f'\n    Description: {desc}'
    h4(result)


timeComplexity("value", "desc")

def spaceComplexity(value, desc):
    result = f' 💾 Space Complexity: Approximately {value}'

    if (desc):
        result += f'\n    Description: {desc}'
    h4(result)

spaceComplexity("value", "desc")

def print_h1(text):
    h1(f"\n{'=' * 40}\n{text}\n{'=' * 40}")


def print_h2(text):
    h2(f"\n{'-' * 35}\n{text}\n{'-' * 35}")


def print_h3(text):
    h3(f"\n{text}\n{'-' * 30}")


def print_h4(*text):
    combined_text = " ".join(str(t) for t in text)  # Join all elements of text into one string
    h4(f"\n{combined_text}\n{'-' * 25}")

def print_h5(text):
    h5(f"\n{text}\n{'-' * 20}")

def print_h6(*text):
    combined_text = " ".join(str(t) for t in text)  # Join all elements of text into one string
    h6(f"\n{combined_text}\n{'-' * 15}")

def print_span(*text):
    combined_text = " ".join(str(t) for t in text)  # Join all elements of text into one string
    # Using ANSI escape code for bold text
    h4(f"> \033[1m{combined_text}\033[0m")

def print_ordered_list(items):
    for i, item in enumerate(items, start=1):
        h5(f"{i}. {item}")


def print_bullet_list(items, bullet_char='*'):
    for item in items:
        print(f"{bullet_char} {item}")


def print_blockquote(items, indent_char='> ', emoji='💬', new_line = False):
    if (new_line):
        print('\n')
    for item in items:
        h6(f"{emoji} {indent_char}{item}")


def pretty_json(input):
    pprint.pprint(input, width=50, indent=2)

def print_tabular_list(data, col_widths=None):
    # Calculate column widths based on the data if not provided
    if col_widths is None:
        col_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

    def print_divider():
        line = "+" + "+".join("-" * width for width in col_widths) + "+"
        h4(line)

    def print_header_divider():
        line = "-" * (sum(col_widths) + len(col_widths) - 1)
        h5(line)

    # Print the header row
    print_divider()
    header = data[0]
    formatted_header = "|".join(
        f"{item:<{col_widths[i]}}" for i, item in enumerate(header))
    h6("|" + formatted_header + "|")
    print_header_divider()

    # Print the rest of the rows
    for row in data[1:]:
        formatted_row = "|".join(
            f"{item:<{col_widths[i]}}" for i, item in enumerate(row))
        h5("|" + formatted_row + "|")
        print_header_divider()
