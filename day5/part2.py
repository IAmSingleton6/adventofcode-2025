from __future__ import annotations

class Inventory:
    def __init__(self, ranges: list[tuple[int, int]], ids: list[int]) -> None:
        self.ranges: list[tuple[int, int]] = ranges
        self.ids: list[int] = ids
    
    def getFreshCountFromRanges(self) -> int:
        range_objs = merge_ranges([Range(r) for r in self.ranges])
        return sum(r.get_span() for r in range_objs)


class Range:
    def __init__(self, range: tuple[int, int]) -> None:
        self.start: int = range[0]
        self.end: int = range[1]
    
    def get_span(self) -> int:
        return self.end - self.start + 1

    def merge_with(self, other: Range) -> Range:
        new_start = min(self.start, other.start)
        new_end = max(self.end, other.end)
        return Range((new_start, new_end))
    
    def overlaps_with(self, other: Range) -> bool:
        return not (self.end < other.start or self.start > other.end)


def merge_ranges(ranges: list[Range]) -> list[Range]:
    if not ranges:
        return []
    
    ranges.sort(key=lambda r: r.start)
    merged: list[Range] = [ranges[0]]

    for current in ranges[1:]:
        last = merged[-1]

        if last.overlaps_with(current):
            last.start = min(last.start, current.start)
            last.end   = max(last.end, current.end)
        else:
            merged.append(current)

    return merged

def parse_data(path: str) -> Inventory:
    with open(path) as f:
        data_split = f.read().strip().split("\n\n")

        data_ids = [int(x) for x in data_split[1].splitlines()]
        data_ranges = [tuple(map(int, line.split("-"))) for line in data_split[0].splitlines()]

        return Inventory(ranges=data_ranges, ids=data_ids)

def main():
    data = parse_data("input.txt")
    print("Fresh IDs count:", data.getFreshCountFromRanges())

if __name__ == "__main__":
    main()