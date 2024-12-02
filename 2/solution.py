def levelsgpoingupordown(levels):
    increasing = all(
        levels[i] < levels[i + 1] and 1 <= levels[i + 1] - levels[i] <= 3
        for i in range(len(levels) - 1)
    )
    decreasing = all(
        levels[i] > levels[i + 1] and 1 <= levels[i] - levels[i + 1] <= 3
        for i in range(len(levels) - 1)
    )
    return increasing or decreasing


def safe(filename):
    with open(filename, "r") as file:
        reports = file.readlines()

    safe_count = 0
    for report in reports:
        levels = list(map(int, report.strip().split()))
        if levelsgpoingupordown(levels) or safewithoutone(levels):
            safe_count += 1

    return safe_count


def safewithoutone(levels):
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1 :]
        if levelsgpoingupordown(new_levels):
            return True
    return False


if __name__ == "__main__":
    filename = "input.txt"
    safe_reports = safe(filename)
    print(f"Number of safe reports: {safe_reports}")
