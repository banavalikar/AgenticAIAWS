import sys
from typing import List

def validate_and_convert(num_str: str) -> int:
    try:
        return int(num_str)
    except ValueError:
        print(f"Error: '{num_str}' is not a valid integer.")
        return None

def main(args: List[str]) -> None:
    if len(args) < 2:
        print("Error: No numbers provided.")
    else:
        numbers = [validate_and_convert(arg) for arg in args[1:]]
        numbers = [num for num in numbers if num is not None]
        for num in numbers:
            print(f"Number: {num}")

if __name__ == "__main__":
    main(sys.argv)