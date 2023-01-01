def calculate():
    # dictionary of available operations
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    while True:
        # get user input
        input_str = input("Enter an operation (q to quit): ")

        # check if the user wants to quit
        if input_str == "q":
            return("calculate() quit")           

        # split the input string into the operation and operands
        operation, *operands = input_str.split()

        # convert the operands to floats
        operands = [float(x) for x in operands]

        # check if the operation is valid
        if operation not in operations:
            print("Invalid operation")
            continue

        # perform the operation
        result = operations[operation](*operands)

        # print the result
        print(f"Result: {result}")
        return(str(result))

# call the calculate function
# calculate()
# test git 