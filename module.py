import sys
import subprocess
import os

def run_python_file(file_path):
    # Convert file path to module path
    module_path = file_path.replace('/', '.').replace('\\', '.')
    module_path = os.path.splitext(module_path)[0]  # Remove file extension

    command = [sys.executable, "-m", module_path]

    print("Executing command:", ' '.join(command))
    
    # Run as module
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running module {module_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python runfile.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    run_python_file(file_path)
