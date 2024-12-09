# Part 1: Rearrange files and calculate checksum

# Step 1: Read the disk map from the input file
with open("input.txt") as f:
    disk_map = list("".join(x.strip() for x in f))

# Step 2: Expand the disk map into a list of blocks
expanded = []
for i, r in enumerate(disk_map):
    if i % 2 == 0:
        for k in range(int(r)):
            expanded.append(f"{i // 2}")
    else:
        for k in range(int(r)):
            expanded.append(".")

# Step 3: Move all files to the left, making free space contiguous
free_ptr = 0
end_ptr = len(expanded) - 1

while free_ptr < end_ptr:
    while expanded[free_ptr] != ".":
        free_ptr += 1
    while expanded[end_ptr] == ".":
        end_ptr -= 1

    if free_ptr < end_ptr:
        expanded[free_ptr] = expanded[end_ptr]
        expanded[end_ptr] = "."
        free_ptr += 1
        end_ptr -= 1

# Step 4: Calculate the checksum
s = [e for e in expanded if e != "."]
checksum_part1 = sum(i * int(k) for i, k in enumerate(s))
print("Checksum (Part 1):", checksum_part1)

# Part 2: Rearrange files using a different approach and calculate checksum

# Step 1: Read the disk map from the input file
with open("input.txt") as f:
    disk_code = [int(i) for i in "".join(x.strip() for x in f)]

# Step 2: Parse the disk map into files and free spaces
d = {}
frees = []
counter = 0

for i, r in enumerate(disk_code):
    start, end = counter, counter + r
    if i % 2 == 0:
        d[i // 2] = (start, end)
    elif r > 0:
        frees.append((start, end))
    counter += r

# Step 3: Move files to the left, making free space contiguous
idx_ptr = max(d.keys())

while idx_ptr >= 0:
    file_start, file_end = d[idx_ptr]
    file_len = file_end - file_start

    free_ptr = 0
    while free_ptr < len(frees):
        gap_start, gap_end = frees[free_ptr]
        if gap_start >= file_start:
            break

        gap_len = gap_end - gap_start
        if file_len <= gap_len:
            frees.pop(free_ptr)

            new_file_start, new_file_end = gap_start, gap_start + file_len
            new_gap_start, new_gap_end = new_file_end, gap_end

            d[idx_ptr] = (new_file_start, new_file_end)
            if new_gap_start != new_gap_end:
                frees.insert(free_ptr, (new_gap_start, new_gap_end))
            break
        else:
            free_ptr += 1

    idx_ptr -= 1

# Step 4: Calculate the checksum
checksum_part2 = 0
for k, (start, end) in d.items():
    checksum_part2 += sum(k * i for i in range(start, end))
print("Checksum (Part 2):", checksum_part2)
