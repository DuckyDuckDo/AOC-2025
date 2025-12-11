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

def get_all_paths2(graph):
    """
    Given a graph, we need to find all paths from svr to out that visits both dac and fft
    """
    start = "svr"
    end = "out"

    queue = deque([(start, False, False)]) # (node, passed_dac, passed_fft)
    num_paths = 0

    while queue:
        curr_node, passed_dac, passed_fft = queue.popleft()
        if curr_node == end and passed_dac and passed_fft:
            num_paths += 1
        
        if curr_node == "dac":
            passed_dac = True
        if curr_node == "fft":
            passed_fft = True

    for neighbor in graph[curr_node]:
            queue.append((neighbor, passed_dac, passed_fft))
    
    return num_paths
        


for file in test_files:
    graph = parse_inputs(file)
    num_paths = get_all_paths(graph)
    num_paths2 = get_all_paths2(graph)
    print(num_paths, num_paths2)