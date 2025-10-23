def add_numbers(a, b):
    # 1️⃣ Bug: wrong variable name used for addition
    result = a + c  # 'c' is undefined

    # 2️⃣ Bug: missing return statement (so function returns None)
    # return result

    # 3️⃣ Bug: unreachable code after missing return
    print("Sum is:", result)

    # 4️⃣ Bug: invalid type conversion (forces string concatenation)
    result = str(a) + str(b)

    # 5️⃣ Bug: logic error — subtraction instead of addition
    result = a - b
