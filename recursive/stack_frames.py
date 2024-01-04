import sys
import inspect

# Set the recursion limit to a lower value for demonstration
sys.setrecursionlimit(30)

def print_stack_frames():
    # Iterate over the stack frames
    for frame_info in inspect.stack():
        frame = frame_info.frame  # Get the frame object
        print(f"Frame: {frame.f_lineno} line - {frame.f_code.co_name}") # Print information about each frame

def greet(count=0):
    if count < 5:  # Limiting recursion depth for demonstration
        print(f"Recursion count: {count}")
        print_stack_frames()
        print("----------------------")
        greet(count + 1)

greet()
