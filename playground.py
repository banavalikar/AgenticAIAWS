def add_nums(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Invalid input. Please provide numbers.")
        return None
    result = a + b
    print("Sum is {}".format(result))
    return result