def add_nums(a, b):
    sum = a + c        # ❌ Bug 1: 'c' is undefined (NameError)
    print("Sum is" + sum)  # ❌ Bug 2: trying to concatenate str + int
    return a - b       # ❌ Bug 3: wrong operation (should be addition)
