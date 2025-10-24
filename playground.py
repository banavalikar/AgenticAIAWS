def add_nums(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Input values must be numbers.")
    result = a + b
    return result