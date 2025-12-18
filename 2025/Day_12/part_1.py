INPUT_PATH = "2025/Day_12/input.txt"


if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()

    shapes = {}
    last_shape = None
    regions = []

    for line in lines:
        line = line.strip()
        if line == "":
            continue
        elif "#" in line or "." in line:
            shapes[last_shape].append(list(line))
        else:
            split = line.split(":")
            if split[-1] == "":
                last_shape = int(split[0])
                shapes[last_shape] = []
            else:
                area = tuple([int(x) for x in split[0].split("x")])
                regions.append((area, [int(x) for x in split[-1].strip().split()]))

    # === SOLVE ===
    result = 0

    for size, presents in regions:
        width = size[0]
        height = size[1]

        total_area = width * height

        if 9 * sum(presents) <= total_area:
            result += 1

    # === OUTPUT ===
    print(result)
