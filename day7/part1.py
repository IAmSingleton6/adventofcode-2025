def parse_data(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()

def find_split_total(rows: list[str]) -> int:
    start_beam_index = rows[0].index("S")
    beam_indexes = { start_beam_index }
    split_total = 0

    for row in rows[1:]:
        splitter_indexes = { i for i, char in enumerate(row) if char == "^" }
        splits = beam_indexes & splitter_indexes
        split_total += len(splits)

        for split in splits:
            beam_indexes.remove(split)
            if split - 1 >= 0:
                beam_indexes.add(split - 1)
            if split + 1 < len(row):
                beam_indexes.add(split + 1)
    
    return split_total

def main():
    rows = parse_data("input.txt")
    split_total = find_split_total(rows)
    print(f"Split total: {split_total}")

if __name__ == "__main__":
    main()