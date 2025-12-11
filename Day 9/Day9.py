# Part 1: Given a list of (x, y) pairs, return two representing opposite corners of a rectangle that returns the highest area

# Part 2: Given a list of (x, y) pairs, they form a shape, now from any pair of points, choose a rectangle, but the rectangle must be within the shape
from collections import defaultdict

test_files =  [
    'test.txt',
    # 'input.txt',
               ]

def parse_inputs(file):
    points = []
    with open(file) as file:
        for line in file.readlines():
            points.append([int(x) for x in line.strip("\n").split(",")])
    return points

def get_max_rectangle(points):
    """
    Given an array of points, brute force generate all pairs and find the max rectangle area from the pair
    using abs((y2 - y1) * (x2 - x1))
    """
    max_area = float('-inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            max_area = max(max_area, abs((points[i][0] - points[j][0] + 1) * (points[i][1] - points[j][1] + 1)))
    return max_area

# Part 2
# Id say, form the border, flood fill the middle, and then check pairs and check if all corners are within the border
def form_grid(points):
    """
    Forms a grid where the points are the red points, and we will connect them to one another
    THIS IS TOO SLOW
    """
    cols = max(points, key = lambda x: x[0])[0]
    rows = max(points, key = lambda x: x[1])[1]

    grid = [["." for _ in range(cols + 1)] for _ in range(rows + 1)]
    print("Grid init")

    prev = points[-1]
    for col, row in points:
        grid[row][col] = "#"
        same_row_as_prev = row == prev[1]
        if same_row_as_prev:
            start, end = min(col, prev[0]), max(col, prev[0])
            for sub_col in range(start + 1, end):
                grid[row][sub_col] = "X"
        else:
            start, end = min(row, prev[1]), max(row, prev[1])

            for sub_row in range(start + 1, end):
                grid[sub_row][col] = "X"
        prev = col, row
    print("Grid Formed")
    return grid

def get_interval_maps(points):
    """
    Because the points connect from the previous point, we can form maps of valid intervals
    """

    row_maps = defaultdict(list) # Each key is a row, with columns in interval (inclusive) that are valid
    col_maps = defaultdict(list) # Each key is a col, with rows in interval (inclusive) that are valid

    prev = points[-1]
    for row, col in points:
        is_same_row = row == prev[0]
        if is_same_row:
            row_maps[row].append((tuple(sorted([col, prev[1]]))))
        else:
            col_maps[col].append((tuple(sorted([row, prev[0]]))))
        prev = [row, col]
    return row_maps, col_maps

def check_point(row, col, row_maps, col_maps):
    """
    Given a point, check their validity in row intervals and col intervals
    """
    col_valid = False
    row_valid = False
    for col_interval in row_maps[row]:
        if col >= col_interval[0] and col <= col_interval[1]:
            col_valid = True
            break
    
    for row_interval in col_maps[col]:
        if row >= row_interval[0] and row <= row_interval[1]:
            row_valid = True
    return col_valid or row_valid

def check_interal(row, col, row_maps, col_map):
    """
    Secondary check of a point if it is within the borders, checks if the points falls in two intervals
    in both row and column directions
    """


def get_max_rectangle2(points, row_maps, col_maps):
    """
    Find the best rectangle form point pairs, if they fall within the valid intervals. 
    """
    max_area = float('-inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            row1, col1 = points[i]
            row2, col2 = points[j]
            if check_point(row1, col2, row_maps, col_maps) and check_point(row2, col1, row_maps, col_maps):
                max_area = max(max_area, abs((points[i][0] - points[j][0] + 1) * (points[i][1] - points[j][1] + 1)))

    return max_area


for file in test_files:
    points = parse_inputs(file)
    result1 = get_max_rectangle(points)
    row_maps, col_maps = get_interval_maps(points)
    result2 = get_max_rectangle2(points, row_maps, col_maps)
    print(result1, result2)


    