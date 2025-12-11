# Part 1: Given a target configuration, buttons to press that switch things on and off, and a joltage setting (unused for Part 1).
# Sum up the minimum # of button presses to achieve each target configuration
# Part 2: 
from collections import deque
import ast

test_files =  [
    'test.txt',
    # 'input.txt',
               ]

def parse_inputs(file):
    problems = []
    with open(file) as file:
        for line in file.readlines():
            problems.append(line.strip("\n").split())
    return problems

def parse_problem(problem):
    """
    Parse the problem string
    """

    configuration = list(problem[0])[1:-1]
    buttons = list(problem[1:len(problem) - 1])
    buttons = [ast.literal_eval(x) for x in buttons]
    for i, button in enumerate(buttons):
        if isinstance(button, int):
            buttons[i] = (button, )
    start_config = [x == "#" for x in configuration]
    return start_config, buttons

def solve_problem(problem):
    """
    Given a problem that is an array of configuration, n buttons, and a joltage, find the minimum number of button presses to achieve
    configuration (aka go from configuration to an all off state)
    """
    start_config, buttons = parse_problem(problem)
    end_config = [False] * len(start_config)

    # Keeps track of visited in case we hit cycles
    visited = set()

    # Perform a BFS, with start, end and transition being processed accordingly
    queue = deque([(0, start_config)])
    while queue:
        curr_step, curr_config = queue.popleft()
        if curr_config == end_config:
            return curr_step

        visited.add(curr_config)
        







for file in test_files:
    problems = parse_inputs(file)
    for problem in problems:
        solve_problem(problem)