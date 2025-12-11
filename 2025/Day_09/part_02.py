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


def intersects(min_x, min_y, max_x, max_y, edges):
    for p1, p2 in edges:
        i_min_x, i_max_x = sorted((p1.x, p2.x))
        i_min_y, i_max_y = sorted((p1.y, p2.y))

        # Bounding-box overlap test
        if min_x < i_max_x and max_x > i_min_x and min_y < i_max_y and max_y > i_min_y:
            return True
    return False


def manhattan_distance(a: Point, b: Point):
    return abs(a.x - b.x) + abs(a.y - b.y)


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

    edges = []
    for i in range(len(points) - 1):
        edges.append((points[i], points[i + 1]))
    edges.append((points[0], points[-1]))

    for i, p_1 in enumerate(points):
        for p_2 in points[i+1:]:

            min_x, max_x = sorted((p_1.x, p_2.x))
            min_y, max_y = sorted((p_1.y, p_2.y))

            # Skip rectangle if it intersects an edge
            if intersects(min_x, min_y, max_x, max_y, edges):
                continue

            result = max(result, rectangle_area(p_1, p_2))

    # === OUTPUT ===
    print(result)