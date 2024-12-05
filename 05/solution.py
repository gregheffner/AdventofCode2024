def check_sequence(sequence, rules):
    for rule in rules:
        first, second = rule
        if first in sequence and second in sequence:
            if sequence.index(first) > sequence.index(second):
                return False
    return True

def rearrange_sequence(sequence, rules):
    def compare(x, y):
        for first, second in rules:
            if (x == first and y == second) or (x == second and y == first):
                return -1 if x == first else 1
        return 0

    return sorted(sequence, key=lambda x: [compare(x, y) for y in sequence])

def main():
    rules = []
    sequences = []
    reading_rules = True

    # Read rules and sequences from input.txt
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                reading_rules = False
                continue

            if reading_rules:
                try:
                    first, second = map(int, line.split('|'))
                    rules.append((first, second))
                except ValueError:
                    print(f"Skipping invalid rule: {line}")
            else:
                try:
                    sequence = list(map(int, line.split(',')))
                    sequences.append(sequence)
                except ValueError:
                    print(f"Skipping invalid sequence: {line}")

    valid_sequences = []
    invalid_sequences = []
    for i, sequence in enumerate(sequences):
        if check_sequence(sequence, rules):

            valid_sequences.append(sequence)
        else:

            invalid_sequences.append(sequence)

    valid_middle_sum = 0
    for sequence in valid_sequences:
        middle_index = len(sequence) // 2
        valid_middle_sum += sequence[middle_index]

    invalid_middle_sum = 0
    rearranged_sequences = []
    for sequence in invalid_sequences:
        rearranged_sequence = rearrange_sequence(sequence, rules)
        rearranged_sequences.append(rearranged_sequence)
        middle_index = len(rearranged_sequence) // 2
        invalid_middle_sum += rearranged_sequence[middle_index]

    print(f"Sum of middle numbers of valid sequences: {valid_middle_sum}")
    print(f"Sum of middle numbers of rearranged to be valid sequences: {invalid_middle_sum}")

if __name__ == "__main__":
    main()