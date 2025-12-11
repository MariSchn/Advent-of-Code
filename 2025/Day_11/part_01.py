from collections import defaultdict


INPUT_PATH = "2025/Day_11/input.txt"


if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()

    nodes = defaultdict(list)
    for line in lines:
        label, neighbors = line.split(":")

        for neighbor in neighbors.strip().split(" "):
            nodes[label].append(neighbor.strip())

    # === SOLVE ===
    result = 0

    stack = []
    stack.append("you")

    while stack:
        label = stack.pop()

        for neighbor in nodes[label]:
            if neighbor == "out":
                result += 1
            else:
                stack.append(neighbor)

    # === OUTPUT ===
    print(result)