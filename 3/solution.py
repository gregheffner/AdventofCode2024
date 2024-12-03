import re


def extract_and_multiply(data):
    """
    Extract valid mul(X,Y) instructions from the data, perform the multiplications,
    and return the sum of the results, considering do() and don't() instructions.

    Args:
    data (str): The corrupted memory data as a string.

    Returns:
    int: The sum of all valid multiplications.
    """
    # Regular expression to find valid mul(X,Y) instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Regular expressions to find do() and don't() instructions
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Initialize the sum of results
    total_sum = 0

    # Initialize the state of mul instructions (enabled by default)
    mul_enabled = True

    # Split the data into tokens based on the presence of mul, do, and don't instructions
    tokens = re.split(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", data)

    # Iterate through the tokens
    for token in tokens:
        # Check if the token is a do() instruction
        if re.match(do_pattern, token):
            mul_enabled = True
        # Check if the token is a don't() instruction
        elif re.match(dont_pattern, token):
            mul_enabled = False
        # Check if the token is a valid mul(X,Y) instruction
        elif re.match(pattern, token):
            if mul_enabled:
                # Extract the numbers X and Y
                match = re.match(pattern, token)
                x, y = map(int, match.groups())
                # Perform the multiplication and add to the total sum
                total_sum += x * y

    return total_sum


if __name__ == "__main__":
    # Read the input data from a file
    with open("input.txt", "r") as file:
        data = file.read()

    # Calculate the sum of all valid multiplications
    result = extract_and_multiply(data)

    # Print the result
    print(f"The sum of all valid multiplications is: {result}")
