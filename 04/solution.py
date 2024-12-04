def calc(log, values, mode):
    grid = [list(line) for line in values]

    ret = 0
    if mode == 1:
        word = "XMAS"
        directions = [
            (0, 1),  # right
            (0, -1),  # left
            (-1, 0),  # up
            (1, 0),  # down
            (-1, 1),  # up-right
            (-1, -1),  # up-left
            (1, -1),  # down-left
            (1, 1),  # down-right
        ]

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                for dir in directions:
                    rowIndex, colIndex = dir
                    isXmas = True

                    for charIndex in range(len(word)):
                        rowOffset = row + (rowIndex * charIndex)
                        colOffset = col + (colIndex * charIndex)

                        if (
                            rowOffset < 0
                            or rowOffset >= len(grid)
                            or colOffset < 0
                            or colOffset >= len(grid[row])
                        ):
                            isXmas = False
                            break

                        if grid[rowOffset][colOffset] != word[charIndex]:
                            isXmas = False
                            break

                    if isXmas:
                        ret += 1
    else:
        directions = [
            [(-1, 1), (1, -1)],  # diagonal up-right and down-left
            [(-1, -1), (1, 1)],  # diagonal up-left and down-right
        ]

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != "A":
                    continue

                isXmas = True

                for dir in directions:
                    row1Index = row + dir[0][0]
                    col1Index = col + dir[0][1]

                    row2Index = row + dir[1][0]
                    col2Index = col + dir[1][1]

                    if (
                        row1Index < 0
                        or row1Index >= len(grid)
                        or col1Index < 0
                        or col1Index >= len(grid[row])
                        or row2Index < 0
                        or row2Index >= len(grid)
                        or col2Index < 0
                        or col2Index >= len(grid[row])
                    ):
                        isXmas = False
                        break

                    if (
                        grid[row1Index][col1Index] == "M"
                        and grid[row2Index][col2Index] == "S"
                    ) or (
                        grid[row1Index][col1Index] == "S"
                        and grid[row2Index][col2Index] == "M"
                    ):
                        continue

                    isXmas = False
                    break

                if isXmas:
                    ret += 1

    return ret


def run(log, values):
    log(calc(log, values, 1))
    log(calc(log, values, 2))


if __name__ == "__main__":
    import os
    import sys

    def find_input_file():
        for fn in sys.argv[1:] + [
            "input.txt",
        ]:
            for dn in [[], ["Puzzles"], ["..", "Puzzles"]]:
                cur = os.path.join(*(dn + [fn]))
                if os.path.isfile(cur):
                    return cur

    fn = find_input_file()
    with open(fn) as f:
        values = [x.strip("\r\n") for x in f.readlines()]
    run(print, values)
