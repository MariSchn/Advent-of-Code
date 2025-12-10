from dataclasses import dataclass

INPUT_PATH = "2025/Day_09/input.txt"


@dataclass
class Point:
    x: int
    y: int


def rectangle_area(p_1: Point, p_2: Point):
    width = max(p_1.x, p_2.x) - min(p_1.x, p_2.x) + 1
    height = max(p_1.y, p_2.y) - min(p_1.y, p_2.y) + 1

    return width * height


if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()

    points = []
    for line in lines:
        x, y = line.split(",")
        points.append(Point(int(x), int(y)))

    # === SOLVE ===
    result = 0

    for i, p_1 in enumerate(points):
        for p_2 in points[i+1:]:
            result = max(result, rectangle_area(p_1, p_2))

    # === OUTPUT ===
    print(result)