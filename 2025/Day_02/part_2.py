INPUT_PATH = "2025/Day_02/input.txt"

if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()

    ranges = []
    for _range in lines[0].split(","):
        start, end = map(int, _range.split("-"))
        ranges.append((start, end))
 
    # === SOLVE ===
    result = 0
    for start, end in ranges:
        print(f"Processing {start} - {end}")
        for current in range(start, end + 1):
            s = str(current)

            for sub_s_len in range(1, len(s) // 2 + 1):
                # Check if we can split s into sub_s_len long parts
                if len(s) % sub_s_len != 0:
                    continue
                
                chunks = [s[i:min(len(s), i + sub_s_len)] for i in range(0, len(s), sub_s_len)]

                if all(chunks[0] == chunk for chunk in chunks):
                    result += current
                    
                    # Prevent number from being added multiple times
                    break

    # === OUTPUT ===
    print("Sum of all invalid ids: ", result)
