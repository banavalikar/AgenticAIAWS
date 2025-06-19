import sys

if len(sys.argv) < 2:
    print("Error: No numbers provided.")
else:
    numbers = [int(num) for num in sys.argv[1:]]
    for num in numbers:
        print(f"Number: {num}")
