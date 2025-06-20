import re

def sanitize_input(input_str):
    # Remove or escape potentially dangerous characters
    return re.sub(r'[^\w\s]', '', input_str.translate(str.maketrans({'<': '&lt;', '>': '&gt;'})))

numbers = sanitize_input(input('Enter numbers: '))
for i in range(len(numbers)):
    print(f'Number: {numbers[i]}')