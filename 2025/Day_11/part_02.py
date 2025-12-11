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
    cache = {}

    def count_paths(label, visited_dac, visited_fft):
        # Check cache
        key = (label, visited_dac, visited_fft)
        if key in cache:
            return cache[key]

        # If we reached the end
        if label == "out":
            return int(visited_dac and visited_fft)

        total = 0
        for neighbor in nodes[label]:
            if neighbor == "dac":
                total += count_paths(neighbor, True, visited_fft)
            elif neighbor == "fft":
                total += count_paths(neighbor, visited_dac, True)
            else:
                total += count_paths(neighbor, visited_dac, visited_fft)

        # Store in cache
        cache[key] = total
        return total
    
    result = count_paths("svr", False, False)
    
    # === OUTPUT ===
    print(result)