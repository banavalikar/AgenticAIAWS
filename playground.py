import sys

if len(sys.argv) < 2:
    print("Error: No numbers provided.")
else:
    numbers = []
    for num_str in sys.argv[1:]:
        try:
            num = int(num_str)
        except ValueError:
            print(f"Error: '{num_str}' is not a valid integer.")
            continue
        numbers.append(num)

    for num in numbers:
        print(f"Number: {num}")