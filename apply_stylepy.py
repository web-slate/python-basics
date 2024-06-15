import os
import sys

# Import the stylepy module
import stylepy

# List of directories to apply stylepy
directories = [
    "basics",
    "bits",
    "classes",
    "controls",
    "data_structures",
    "data_types",
    "defs",
    "functions",
    "interview",
    "leetcode",
    "math"
]

def apply_stylepy_to_directory(directory):
    # Assuming stylepy has a function to apply styles, e.g., stylepy.apply(directory)
    print(f"Applying stylepy to {directory}")
    stylepy.apply(directory)  # Replace this with the actual function call from stylepy

if __name__ == "__main__":
    # Navigate to each directory and apply stylepy
    for dir in directories:
        if os.path.isdir(dir):
            apply_stylepy_to_directory(dir)
        else:
            print(f"Directory {dir} does not exist.")
