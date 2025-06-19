def print_numbers():
    numbers = [1, 2, 3, 4, 5]
    
    for i in range(numbers):  # ❌ Error: 'range' requires an integer, not a list
        print(f"Number: {i}")
        return

print_numbers()
#attempt12
