def parse_map(map_str):
    """
    Parses the input topographic map string into a 2D array of integers.

    Args:
        map_str (str): The input topographic map as a string.

    Returns:
        list: A 2D list representing the topographic map.
    """
    return [list(map(int, line)) for line in map_str.strip().split("\n")]


def find_trailheads(map_data):
    """
    Finds all trailheads (positions with height 0) in the topographic map.

    Args:
        map_data (list): The 2D list representing the topographic map.

    Returns:
        list: A list of tuples representing the coordinates of all trailheads.
    """
    trailheads = []
    for r in range(len(map_data)):
        for c in range(len(map_data[0])):
            if map_data[r][c] == 0:
                trailheads.append((r, c))
    return trailheads


# Part 1: Calculate total score of trailheads
def bfs(map_data, start):
    """
    Performs a breadth-first search (BFS) to find all reachable 9-height positions
    from the given trailhead.

    Args:
        map_data (list): The 2D list representing the topographic map.
        start (tuple): The starting coordinates of the trailhead.

    Returns:
        int: The number of reachable 9-height positions.
    """
    from collections import deque

    rows, cols = len(map_data), len(map_data[0])
    queue = deque([start])
    visited = set([start])
    reachable_nines = 0

    while queue:
        r, c = queue.popleft()
        if map_data[r][c] == 9:
            reachable_nines += 1

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if map_data[nr][nc] == map_data[r][c] + 1:
                    queue.append((nr, nc))
                    visited.add((nr, nc))

    return reachable_nines


def calculate_total_score(map_str):
    """
    Calculates the total score of all trailheads in the topographic map.

    Args:
        map_str (str): The input topographic map as a string.

    Returns:
        int: The total score of all trailheads.
    """
    map_data = parse_map(map_str)
    trailheads = find_trailheads(map_data)
    total_score = 0

    for trailhead in trailheads:
        total_score += bfs(map_data, trailhead)

    return total_score


# Part 2: Calculate total rating of trailheads
def dfs(map_data, r, c, visited):
    """
    Performs a depth-first search (DFS) to count all distinct hiking trails
    that reach a 9-height position from the given trailhead.

    Args:
        map_data (list): The 2D list representing the topographic map.
        r (int): The row index of the current position.
        c (int): The column index of the current position.
        visited (set): A set of visited positions.

    Returns:
        int: The number of distinct hiking trails that reach a 9-height position.
    """
    rows, cols = len(map_data), len(map_data[0])
    if map_data[r][c] == 9:
        return 1

    visited.add((r, c))
    trails = 0

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
            if map_data[nr][nc] == map_data[r][c] + 1:
                trails += dfs(map_data, nr, nc, visited)

    visited.remove((r, c))
    return trails


def calculate_total_rating(map_str):
    """
    Calculates the total rating of all trailheads in the topographic map.

    Args:
        map_str (str): The input topographic map as a string.

    Returns:
        int: The total rating of all trailheads.
    """
    map_data = parse_map(map_str)
    trailheads = find_trailheads(map_data)
    total_rating = 0

    for trailhead in trailheads:
        total_rating += dfs(map_data, trailhead[0], trailhead[1], set())

    return total_rating


# Read input from input.txt
with open("input.txt", "r") as file:
    map_str = file.read()

# Part 1: Calculate and print total score
total_score = calculate_total_score(map_str)
print("Total Score:", total_score)

# Part 2: Calculate and print total rating
total_rating = calculate_total_rating(map_str)
print("Total Rating:", total_rating)
