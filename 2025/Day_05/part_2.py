INPUT_PATH = "2025/Day_05/input.txt"

if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()

    fresh_ids = []
    query_ids = []
    reading_fresh = True

    for line in lines:
        line = line.strip()
        if not line:
            reading_fresh = False
            continue

        if reading_fresh:
            start, end = line.split("-")
            fresh_ids.append((int(start), int(end)))
        else:
            query_ids.append(int(line))

    # === SOLVE ===
    result = 0

    # Sort based on start date
    fresh_ids.sort(key=lambda x: x[0])

    # Join all overlapping intervals
    joined_fresh_ids = []
    current_start, current_end = fresh_ids[0]
    for start, end in fresh_ids[1:]:
        if start > current_end:
            # Disjoint intervals -> Add current to list
            joined_fresh_ids.append((current_start, current_end))
            current_start = start

        current_end = max(current_end, end)

    # Add the last remaining (unfinished) inteval
    joined_fresh_ids.append((current_start, current_end))

    # Add ranges together
    for start, end  in joined_fresh_ids:
        result += end - start + 1
    
    # === OUTPUT ===
    print("Number of fresh ingredients:", result)
