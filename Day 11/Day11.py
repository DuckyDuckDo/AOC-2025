# Part 1: Given an adjacency list, find how many paths from the node "you" to the node "out"

# Part 2: Same graph as part 1, need to find all paths from svr to out while passing both dac and fft
from collections import defaultdict, deque
test_files =  [
    'test.txt',
    'test2.txt',
    'input.txt',
               ]


def parse_inputs(file):
    graph = defaultdict(list)
    with open(file) as file:
        for line in file.readlines():
            node, neighbors = line.strip("\n").split(":")
            neighbors = neighbors.split()
            for neighbor in neighbors:
                graph[node].append(neighbor)
    
    return graph

def get_all_paths(graph):
    """
    Given a graph, get all possible paths from one node to the other
    Just a simple BFS
    """
    start = "you"
    end = "out"

    queue = deque([start])
    num_paths = 0
    while queue:
        curr_node = queue.popleft()
        if curr_node == end:
            num_paths += 1
        
        for neighbor in graph[curr_node]:
            queue.append(neighbor)
    
    return num_paths

def get_all_paths2(node, passed_dac = False, passed_fft = False, memo = defaultdict(int)):
    """
    Given a graph, we need to find all paths from svr to out that visits both dac and fft
    """

    # DFS with Caching
    # Base Case
    if node == "out" and passed_dac and passed_fft:
        return 1
    elif node == "dac":
        passed_dac = True
    elif node == "fft":
        passed_fft = True
    
    # If not memoized already, take the sum of all neighbors and memoize
    if (node, passed_dac, passed_fft) not in memo:
        for neighbor in graph[node]:
            memo[(node, passed_dac, passed_fft)] += get_all_paths2(neighbor, passed_dac, passed_fft, memo)
    
    # Return memoized case
    return memo[(node, passed_dac, passed_fft)]

        


for file in test_files:
    graph = parse_inputs(file)
    num_paths = get_all_paths(graph)
    num_paths2 = get_all_paths2("svr", memo = defaultdict(int))
    print(num_paths, num_paths2)