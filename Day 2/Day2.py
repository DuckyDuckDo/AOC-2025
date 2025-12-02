# Part 1: Given interval ranges, we need to sum up all numbers in the ranges in which the first half == the second half

# Part 2: Invalid numbers are now any that are made up of a repeated sequence any number of times

test_files =  [
    'test.txt',
    'input.txt',
               ]

def parse_inputs(file):
    input = [] # an array of tuples of intervals (low, high)
    with open(file) as file:
        data = file.readlines()[0].strip("\n")
        data = data.split(",")
        for range in data:
            low, high = range.split('-')
            input.append((low, high))
    
    return input

def check_invalid(string):
    """
    Returns whether the first half of the string is equivalent to the second half
    """
    if len(string) % 2 != 0:
        return False
    
    return string[:len(string)//2] == string[len(string)//2:]

def build_sequence(string, substring):
    """
    Checks that we can build the original substring by concatenating together the substring
    """
    if len(string) % len(substring) != 0:
        return False
    return string == substring * (len(string) // len(substring))

def check_invalid2(string):
    """
    Finds sequences of lengths that evenly divide into the len of the string, concatenate them together and see if they get original nubmer
    """
    n = len(string)
    curr_substring = ""
    # Only care about sequences up until the first half of the string
    for i in range(n//2):
        curr_substring += string[i]
        # with current substring, check if we can build the full string
        if build_sequence(string, curr_substring):
            return True
    
    return False


def process_interval(low, high):
    """
    Given an interval between low and high inclusive, process for invalid numbers and return the sum of them
    """
    sum_of_invalid1, sum_of_invalid2 = 0, 0
    for num in range(int(low), int(high) + 1):
        # Checks for part 1
        if check_invalid(str(num)):
            sum_of_invalid1 += num

        # Checks for part 2
        if check_invalid2(str(num)):
            sum_of_invalid2 += num

    return sum_of_invalid1, sum_of_invalid2

# Solver
for file in test_files:
    # Get intervals from input files
    intervals = parse_inputs(file)
    result1, result2 = 0, 0

    # Loop through each interval and add any invalids to the sum
    for low, high in intervals:
        sum1, sum2 = process_interval(low, high)
        result1 += sum1
        result2 += sum2
        
    print(result1, result2)