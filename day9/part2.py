Point = tuple[int, int]

class Rectangle:
    x_min: int
    x_max: int
    y_min: int
    y_max: int

    def __init__(self, p1: Point, p2: Point) -> None:
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        self.x_min, self.x_max = min(x1, x2), max(x1, x2)
        self.y_min, self.y_max = min(y1, y2), max(y1, y2)

    def overlaps_with(self, other: "Rectangle") -> bool:
        return not (
            self.x_max <= other.x_min
            or other.x_max <= self.x_min
            or self.y_max <= other.y_min
            or other.y_max <= self.y_min
        )

    def area(self) -> int:
        x_len = self.x_max - self.x_min + 1
        y_len = self.y_max - self.y_min + 1
        return x_len * y_len


def parse_data(path: str) -> list[Point]:
    with open(path) as f:
        lines = f.read().splitlines()
        return [tuple(map(int, line.split(','))) for line in lines]

def main():
    red_tile_coordinates = parse_data("input.txt")
    corners = list(red_tile_coordinates)
    edges = [Rectangle(corners[i], corners[(i+1) % len(corners)]) for i in range(len(corners))]

    largest_area = max(
        rect.area()
        for i in range(len(corners))
        for j in range(i + 1, len(corners))
        if not any((rect := Rectangle(corners[i], corners[j])).overlaps_with(edge) for edge in edges)
    )

    print(f"Largest area: {largest_area}")

if __name__ == "__main__":
    main()