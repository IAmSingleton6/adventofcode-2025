def parse_data(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()

def find_timeline_count(rows: list[str]) -> int:
    start_beam_index = rows[0].index("S")
    return get_timeline(start_beam_index, rows[1:])

def get_timeline(beam_index: int, rows: list[str]) -> int:
    memo = {}  

    def helper(beam_index: int, row_index: int) -> int:
        if row_index >= len(rows) or beam_index < 0 or beam_index >= len(rows[row_index]):
            return 1

        key = (beam_index, row_index)
        if key in memo:
            return memo[key]

        for ri in range(row_index, len(rows)):
            row = rows[ri]
            splitter_positions = {col for col, char in enumerate(row) if char == "^"}

            if beam_index in splitter_positions:
                right = helper(beam_index + 1, ri + 1)
                left  = helper(beam_index - 1, ri + 1)
                memo[key] = right + left
                return memo[key]

        # No splitter 
        memo[key] = 1
        return 1

    return helper(beam_index, 0)

def main():
    rows = parse_data("input.txt")
    split_total = find_timeline_count(rows)
    print(f"Split total: {split_total}")

if __name__ == "__main__":
    main()