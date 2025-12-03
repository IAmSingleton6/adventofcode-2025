def is_invalid(id: int) -> bool:
    str_id = str(id)

    str_len = len(str_id)
    if str_len % 2 != 0:
        return False
    
    start_str = str_id[str_len // 2:]
    end_str = str_id[:str_len // 2]

    return start_str == end_str


def parse_data(file_path) -> list[tuple[int, int]]:
    with open(file_path, 'r') as file:
        content = file.read()
    rangeStrs = content.split(",")
    return [tuple(map(int, x.split("-"))) for x in rangeStrs]


def main():
    ranges = parse_data("input.txt")
    invalid_ids = []

    for range_start, range_end in ranges:
        print(range_start)
        print(range_end)
        print("")
        for i in range(range_start, range_end + 1):
            if is_invalid(i):
                invalid_ids.append(i)
    
    invalid_count = sum(int(x) for x in invalid_ids)
    print(len(invalid_ids))
    print(invalid_count)


if __name__ == "__main__":
    main()