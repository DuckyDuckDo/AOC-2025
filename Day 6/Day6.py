# Part 1: Given a row of numbers and a row of operations, perform the operations by column and return the sums

# Part 2: Parse the input file until there are empty strings, collect all nums and perform all operationsx

test_files =  [
    'test.txt',
    'input.txt',
               ]

def parse_inputs(file):
    inputs1 = [] # an array of tuples of intervals (low, high)
    inputs2 = [] # array of lines 
    with open(file) as file:
        for line in file.readlines():
            inputs1.append(line.split())
            inputs2.append(line.strip("\n"))
    return inputs1, inputs2

def process_problems1(inputs):
    """
    Given an array of arrays, where each column is a different problem, and the last row is the operation, perform the operations and sum
    the results
    """
    cols = len(inputs[0])
    rows = len(inputs)
    total_sum = 0
    # Loop through by columns
    for col in range(cols):
        nums = []
        # For each row grab the appropriate number from that column
        for row in range(rows):
            # Sort out numbers from operations
            try: 
                nums.append(int(inputs[row][col]))
            except:
                nums.append(inputs[row][col])

        # Perform the operation and sum up the results
        if nums[-1] == "+":
            total_sum += sum(nums[:-1])
        elif nums[-1] == "*":
            product = 1
            for num in nums[:-1]:
                product *= num
            total_sum += product

    return total_sum

def process_operation(nums, operation):
    """
    Perform the column wise operation digit wise 64, 23, 314, + becomes 623 + 431 + 4
    123, 45, 6 becomes 1 + 24 + 356
    """    
    total_sum = 0
    if operation == "+":
        total_sum += sum(nums)
    elif operation == "*":
        product = 1
        for num in nums:
            product *= num
        total_sum += product
    return total_sum

def process_problems2(inputs):
    """
    Given an array of arrays we need to perform the operations but now we read it by column of digits right to left. 
    So 64 , 23 , 314, + becomes 623 + 431 + 4, while 123, 45,  6, * becomes 1 * 24 * 256, based on column of digits placement
    Use process_column to perform the digitwise column operation
    """
    digits = [''] * (len(inputs) - 1)# whatever digit is in a certain column
    current_operation = ""
    current_nums = []
    total_sum = 0
    # Loop through all the columns
    for i in range(len(inputs[0])):
        # Loop through each of the input lines except the last one, update digits and operations
        for j in range(0, len(inputs) - 1):
            digits[j] = inputs[j][i]
        if inputs[-1][i] != " ":
            current_operation = inputs[-1][i]

        # If we reach an empty column and have an operation, perform and sum the operation, and reset both variables
        if len("".join(digits).strip()) == 0 and current_operation in set(["*", "+"]):
            total_sum += process_operation(current_nums, current_operation)
            current_nums = []
            current_operation = ""

        else:
            current_nums.append(int("".join(digits)))

    # Do the final problem that was never processed, because there was never an empty column at the end
    total_sum += process_operation(current_nums, current_operation)
    return total_sum

for file in test_files:
    inputs1, inputs2 = parse_inputs(file)
    result1 = process_problems1(inputs1)
    result2 = process_problems2(inputs2)
    print(result1, result2)