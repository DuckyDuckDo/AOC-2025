# Part 1: Given shapes, and each line has a grid dimension and total number of each shapes to use, sum up all lines that can fit their alloted shapes

test_files =  [
    'test.txt',
    'input.txt',
               ]

TEST_SHAPES = [
                [1, 1, 1, 1, 1, 0, 1, 1, 0], 
                [1, 1, 1, 1, 1, 0, 0, 1, 1], 
                [0, 1, 1, 1, 1, 1, 1, 1, 0], 
                [1, 1, 0, 1, 1, 1, 0, 1, 1], 
                [1, 1, 1, 1, 0, 0, 1, 1, 1],
                [1, 1, 1, 0, 1, 0, 1, 1, 1]
               ]

INPUT_SHAPES = [
                [0, 0, 1, 0, 1, 1, 1, 1, 0],
                [1, 1, 1, 0, 1, 1, 0, 0, 1], 
                [0, 1, 1, 1, 1, 0, 1, 1, 1], 
                [1, 1, 1, 0, 1, 0, 1, 1, 1], 
                [1, 1, 1, 0, 1, 1, 0, 1, 1], 
                [1, 1, 1, 1, 0, 0, 1, 1, 1]
                ]

def parse_inputs(file):
    problems = [] # (grid dimensions, presents allowed)
    with open(file, "r") as f:
        for line in f.readlines():
            grid, presents = line.strip("\n").split(":")
            grid_dimensions = [int(x) for x in grid.split("x")]
            presents = [int(x) for x in presents.strip().split()]
            problems.append((grid_dimensions, presents))
    
    return problems

def fit_in_area(problem, shapes):
    """
    Problem: (grid dimensions, number of each shape)
    Shapes: definition of each shape, index is the shape identity, and the array is the shape itself in 1D
    Function checks if total area of the grid can even fit all of the dots of the shapes necessary
    If False, then we can prune
    """
    x, y = problem[0]
    total_area = x * y
    total_dots = 0
    for shape, frequency in enumerate(problem[1]):
        if frequency > 0:
            total_dots += frequency * sum(shapes[shape])
    return total_dots < total_area

def guarantee_fit(problem):
    """
    Because each shape is at most a 3x3 square, if the grid dimension has enough 3 x 3 regions as shapes allowed, its automatically solvable. 
    If True, we know it is real
    """
    x, y = problem[0]
    total_x = x//3
    total_y = y//3
    return sum(problem[1]) <= (total_x * total_y)

for file in test_files:
    problems = parse_inputs(file)
    shapes = TEST_SHAPES if file == "test.txt" else INPUT_SHAPES
    pruned_count = 0
    result = 0
    for problem in problems:
        if not fit_in_area(problem, shapes):
            pruned_count += 1
        
        if guarantee_fit(problem):
            result += 1
    
    print(result)
    print(pruned_count)
