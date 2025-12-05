class Inventory:
    def __init__(self, ranges: list[tuple[int, int]], ids: list[int]) -> None:
        self.ranges: list[tuple[int, int]] = ranges
        self.ids: list[int] = ids
    
    def getFreshCountFromIds(self) -> int:
        count = 0
        for id in self.ids:
            if any(start <= id <= end for start, end in self.ranges):
                count += 1
        return count


def parse_data(path: str) -> Inventory:
    with open(path) as f:
        data_split = f.read().strip().split("\n\n")

        data_ids = [int(x) for x in data_split[1].splitlines()]
        data_ranges = [tuple(map(int, line.split("-"))) for line in data_split[0].splitlines()]

        return Inventory(ranges=data_ranges, ids=data_ids)

def main():
    data = parse_data("input.txt")
    print("Fresh IDs count:", data.getFreshCountFromIds())

if __name__ == "__main__":
    main()