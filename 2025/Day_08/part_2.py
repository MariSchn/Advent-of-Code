from typing import List


INPUT_PATH = "2025/Day_08/input.txt"


class UnionFindNode:
    def __init__(self, x, y, z, idx, parent=None):
        self.x = x
        self.y = y
        self.z = z

        self.parent = parent
        self.idx = idx

    def get_root(self):
        if self.parent == None:
            return self
        else:
            root = self.parent.get_root()
            self.parent = root

            return root
        
    def __repr__(self):
        return f"Node {self.idx} ({self.x}, {self.y}, {self.z})"


def squared_distance(node_1: UnionFindNode, node_2: UnionFindNode):
    return (node_1.x - node_2.x) ** 2 + (node_1.y - node_2.y) ** 2 + (node_1.z - node_2.z) ** 2

def one_component(nodes: List):
    component = nodes[0].get_root().idx

    for node in nodes:
        if component != node.get_root().idx:
            return False
        
    return True


if __name__ == "__main__":
    # === READ AND PARSE INPUT ===
    with open(INPUT_PATH, "r") as file:
        lines = file.readlines()

    nodes = []
    for i, line in enumerate(lines):
        x, y, z = line.split(",")
        nodes.append(UnionFindNode(int(x), int(y), int(z), i))

    # === SOLVE ===
    result = 1

    # Calculate all distances and sort
    distances = []
    for i, node_i in enumerate(nodes):
        for j, node_j in enumerate(nodes[i + 1:]):
            j += i + 1

            distances.append((
                squared_distance(node_i, node_j),
                node_i, node_j
            ))
    distances.sort(key=lambda x: x[0])

    # Merge until we only have one component left
    for _, node_i, node_j in distances:
        if node_j.get_root() != node_i.get_root():
            node_j.get_root().parent = node_i.get_root()

        if one_component(nodes):
            result = node_i.x * node_j.x
            break

    # === OUTPUT ===
    print(result)