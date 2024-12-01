def inputfiles(filename):
    left_list = []
    right_list = []

    with open(filename, "r") as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    return left_list, right_list


def distance(left_list, right_list):

    left_list.sort()
    right_list.sort()

    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

    return total_distance


def similarity_score(left_list, right_list):
    similarity_score = 0
    for num in left_list:
        count_in_right = right_list.count(num)
        similarity_score += num * count_in_right
    return similarity_score


left_list, right_list = inputfiles("input.txt")


total_distance = distance(left_list, right_list)
print(f"Total Distance: {total_distance}")


similarity_score = similarity_score(left_list, right_list)
print(f"Similarity Score: {similarity_score}")
