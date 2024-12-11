import math
from collections import Counter


# Parses the input string into a list of integers
def parse_input(input_str):
    return list(map(int, input_str.split()))


# Returns the number of digits in a number
def n_digits(n):
    return math.floor(math.log10(n) + 1)


# Splits a number into two halves
def split_in_half(n):
    num_digits = n_digits(n)
    half = 10 ** (num_digits // 2)
    return divmod(n, half)


# Applies the transformation rules to a stone
def blink(n):
    if n == 0:
        return [1]
    elif n_digits(n) % 2 == 0:
        left, right = split_in_half(n)
        return [left, right]
    else:
        return [n * 2024]


# Solves the problem by applying the blink rules for a given number of blinks
def solve(n, stones):
    for _ in range(n):
        stones = [new_stone for stone in stones for new_stone in blink(stone)]
    return len(stones)


# Counts the occurrences of each stone
def count_stones(stones):
    return Counter(stones)


# Applies the blink rules and keeps track of the count of each stone
def blink_with_count(item):
    stone, count = item
    return [(new_stone, count) for new_stone in blink(stone)]


# Solves the problem using a counter to efficiently handle large numbers of stones
def solve_with_count(n, stones):
    counter = count_stones(stones)
    for _ in range(n):
        new_counter = Counter()
        for stone, count in counter.items():
            for new_stone, new_count in blink_with_count((stone, count)):
                new_counter[new_stone] += new_count
        counter = new_counter
    return sum(counter.values())


# Solves the problem for 25 blinks
def solve1(stones):
    return solve_with_count(25, stones)


# Solves the problem for 75 blinks
def solve2(stones):
    return solve_with_count(75, stones)


# Main function to read input from 'input.txt' and print results for 25 and 75 blinks
def main():
    with open("input.txt", "r") as file:
        input_str = file.read()
    stones = parse_input(input_str)
    print(solve1(stones))
    print(solve2(stones))


# Entry point of the script
if __name__ == "__main__":
    main()
