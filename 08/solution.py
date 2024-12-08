"""
This module contains solutions for the Advent of Code 2024, Day 8 challenge.

Functions:
    part1(): Reads input from 'input.txt', processes the data to identify and count antinodes based on specific rules, and prints the result for Part 1.
    part2(): Reads input from 'input.txt', processes the data to identify and count antinodes based on extended rules, and prints the result for Part 2.

Helper Functions:
    try_add_antinode(x, y, antinode_grid, x_bound, y_bound): Marks a position on the grid as an antinode if it is within bounds and not already marked.
    try_add_all_antinodes(original_x, original_y, x_vector, y_vector, antinode_grid, x_bound, y_bound): Marks all positions along a vector direction from a starting point as antinodes if they are within bounds and not already marked.
"""

import re


def try_add_antinode(x, y, antinode_grid, x_bound, y_bound):
    # Check if the position is within bounds and not already marked
    if 0 <= x <= x_bound and 0 <= y <= y_bound and antinode_grid[y][x] != "#":
        # Mark the position as an antinode
        antinode_grid[y] = antinode_grid[y][:x] + "#" + antinode_grid[y][x + 1 :]


def try_add_all_antinodes(
    original_x, original_y, x_vector, y_vector, antinode_grid, x_bound, y_bound
):
    # First direction
    x = original_x
    y = original_y
    while 0 <= x <= x_bound and 0 <= y <= y_bound:
        try_add_antinode(x, y, antinode_grid, x_bound, y_bound)
        x += x_vector
        y += y_vector
    # Second direction
    x = original_x
    y = original_y
    while 0 <= x <= x_bound and 0 <= y <= y_bound:
        try_add_antinode(x, y, antinode_grid, x_bound, y_bound)
        x -= x_vector
        y -= y_vector


def part1():
    # Read the input file
    with open("input.txt") as f:
        lines = [re.findall(r"[A-Za-z0-9.]+", line)[0] for line in f.readlines()]

    # Create a grid from the lines
    antinode_grid = list(lines)

    # Get the bounds of the grid
    x_bound = len(lines[0]) - 1
    y_bound = len(lines) - 1

    # Dictionary to store satellite positions
    satellites = {}

    # Find all satellites and store their positions
    for y_idx, line in enumerate(lines):
        for x_idx, char in enumerate(line):
            if re.match(r"[A-Za-z0-9]", char):
                pos = [x_idx, y_idx]
                if char in satellites:
                    satellites[char].append(pos)
                else:
                    satellites[char] = [pos]

    # Process each satellite to find antinodes
    for satellite in satellites:
        pos_list = satellites[satellite]
        for pos_idx, pos in enumerate(pos_list):
            for compare_pos in pos_list[:pos_idx] + pos_list[pos_idx + 1 :]:
                x_diff = pos[0] - compare_pos[0]
                y_diff = pos[1] - compare_pos[1]
                pot_x1 = pos[0] + x_diff
                pot_y1 = pos[1] + y_diff
                try_add_antinode(pot_x1, pot_y1, antinode_grid, x_bound, y_bound)
                pot_x2 = compare_pos[0] - x_diff
                pot_y2 = compare_pos[1] - y_diff
                try_add_antinode(pot_x2, pot_y2, antinode_grid, x_bound, y_bound)

    # Count the number of antinodes
    count = sum(line.count("#") for line in antinode_grid)

    # Print the result
    print("Part 1 Result:", count)


def part2():
    # Read the input file
    with open("input.txt") as f:
        lines = [re.findall(r"[A-Za-z0-9.]+", line)[0] for line in f.readlines()]

    # Create a grid from the lines
    antinode_grid = list(lines)

    # Get the bounds of the grid
    x_bound = len(lines[0]) - 1
    y_bound = len(lines) - 1

    # Dictionary to store satellite positions
    satellites = {}

    # Find all satellites and store their positions
    for y_idx, line in enumerate(lines):
        for x_idx, char in enumerate(line):
            if re.match(r"[A-Za-z0-9]", char):
                pos = [x_idx, y_idx]
                if char in satellites:
                    satellites[char].append(pos)
                else:
                    satellites[char] = [pos]

    # Process each satellite to find antinodes
    for satellite in satellites:
        pos_list = satellites[satellite]
        for pos_idx, pos in enumerate(pos_list):
            for compare_pos in pos_list[:pos_idx] + pos_list[pos_idx + 1 :]:
                x_diff = pos[0] - compare_pos[0]
                y_diff = pos[1] - compare_pos[1]
                try_add_all_antinodes(
                    pos[0], pos[1], x_diff, y_diff, antinode_grid, x_bound, y_bound
                )

    # Count the number of antinodes
    count = sum(line.count("#") for line in antinode_grid)

    # Print the result
    print("Part 2 Result:", count)


if __name__ == "__main__":
    part1()
    part2()
