def is_invalid(id: int) -> bool:
    str_id = str(id)
    str_len = len(str_id)

    if str_len == 1:
            return False

    # split the string by the divisor evenly
    # ensure every split is identical
    for divisor in range(1, str_len // 2 + 1):
        if str_len % divisor != 0:
            continue

        if _all_divisions_identical(str_id, divisor):
            return True

    return False


def _all_divisions_identical(str_id: str, divisor: int) -> bool:
    str_len = len(str_id)
    first_segment = str_id[0:divisor]

    for i in range(divisor, str_len, divisor):
        segment = str_id[i:i + divisor]
        if segment != first_segment:
            return False

    return True


def parse_data(file_path) -> list[tuple[int, int]]:
    with open(file_path, 'r') as file:
        content = file.read()
    rangeStrs = content.split(",")
    return [tuple(map(int, x.split("-"))) for x in rangeStrs]


def main():
    ranges = parse_data("input.txt")
    invalid_ids = []

    for range_start, range_end in ranges:
        for i in range(range_start, range_end + 1):
            if is_invalid(i):
                invalid_ids.append(i)
    
    invalid_count = sum(int(x) for x in invalid_ids)
    [print(x) for x in invalid_ids]
    print(len(invalid_ids))
    print(invalid_count)


if __name__ == "__main__":
    main()