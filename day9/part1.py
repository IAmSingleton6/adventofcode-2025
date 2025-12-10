Point = tuple[int, int]

def area_of_rectangle(corner_1: Point, corner_2: Point) -> int:
    width = abs(corner_2[0] - corner_1[0]) + 1
    height = abs(corner_2[1] - corner_1[1]) + 1
    return width * height

def parse_data(path: str) -> list[Point]:
    with open(path) as f:
        lines = f.read().splitlines()
        return [tuple(map(int, line.split(','))) for line in lines]

def calculate_largest_area(red_tile_coordinates: list[Point]) -> int:
    largest_area = 0
    n = len(red_tile_coordinates)
    for i in range(n):
        for j in range(i + 1, n):
            area = area_of_rectangle(red_tile_coordinates[i], red_tile_coordinates[j])
            if area > largest_area:
                largest_area = area
    return largest_area

def main():
    red_tile_coordinates = parse_data("input.txt")
    largest_area = calculate_largest_area(red_tile_coordinates)
    print(f"Largest area: {largest_area}")

if __name__ == "__main__":
    main()