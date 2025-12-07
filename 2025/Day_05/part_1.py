INPUT_PATH = "2025/Day_05/input.txt"

"""
Potential Improvements
- Join overlapping intervals
- Binary search for correct interval instead of linear search
"""

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

    for query in query_ids:
        for start, end in fresh_ids:
            if query < start:
                break

            if start <= query <= end:
                result += 1
                break

    # === OUTPUT ===
    print("Number of fresh ingredients:", result)
