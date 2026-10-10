import subprocess
import sys

def RunPy(Filename: str, args: list) -> None:
    """
    RunPy(Filename: str, args: list) -> None
    This function runs a Python file with the given arguments.
    """

    try:
        command = [sys.executable, Filename] + args
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print("Python file executed successfully.")
        else:
            print(f"Error executing Python file: {result.stderr}")

    except FileNotFoundError:
        print(f"File not found: {Filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(" " * 19, "Usage: runpy [Filename] [args...]")
        sys.exit(1)

    filename = sys.argv[1]
    args = sys.argv[2:]

    RunPy(filename, args)