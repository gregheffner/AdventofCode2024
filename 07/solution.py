import itertools
import operator


class Operation:
    @staticmethod
    def concat(a, b):
        pow = 10
        while b >= pow:
            pow *= 10
        return a * pow + b

    @staticmethod
    def apply(op, left, right):
        if op == "add":
            return left + right
        elif op == "mul":
            return left * right
        elif op == "concat":
            return Operation.concat(left, right)
        else:
            raise ValueError("Unknown operation")


class Equation:
    def __init__(self, test_value, numbers):
        self.test_value = test_value
        self.numbers = numbers

    @staticmethod
    def build(input_str):
        left, right = input_str.split(": ")
        test_value = int(left)
        numbers = list(map(int, right.split()))
        return Equation(test_value, numbers)

    def check(self, operations_list):
        operator_count = len(self.numbers) - 1
        base = len(operations_list)
        operator_masks = range(base**operator_count)
        operator_positions = range(operator_count - 1, -1, -1)

        for mask in operator_masks:
            operators = []
            for i in operator_positions:
                index = (mask // (base**i)) % base
                operators.append(operations_list[index])

            first_operand, *rest_operands = self.numbers
            result = first_operand
            for op, operand in zip(operators, rest_operands):
                result = Operation.apply(op, result, operand)
                if result > self.test_value:
                    break

            if result == self.test_value:
                return True
        return False


def build(input_str):
    return [Equation.build(line) for line in input_str.strip().split("\n")]


def total_calibration_result(equations, operations_list):
    return sum(eq.test_value for eq in equations if eq.check(operations_list))


def result_simple(equations):
    return total_calibration_result(equations, ["add", "mul"])


def result_with_concatenation(equations):
    return total_calibration_result(equations, ["add", "mul", "concat"])


def main():
    with open("input.txt", "r") as file:
        input_data = file.read()
    equations = build(input_data)

    print("Part 1:", result_simple(equations))
    print("Part 2:", result_with_concatenation(equations))


if __name__ == "__main__":
    main()
