def parse_data(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def extract_max_joltage(bank: str, battery_count: int) -> int:
    bank_len = len(bank)
    current_index = 0
    window_size = bank_len - battery_count + 1

    final_str = ""

    for _ in range(battery_count):
        window = bank[current_index:current_index + window_size]
        max_digit = -1
        max_index = -1

        for i, joltage in enumerate(window):
            digit = int(joltage)
            if digit > max_digit:
                max_digit = digit
                max_index = i
        
        final_str += str(max_digit)
        current_index += max_index + 1
        window_size -= max_index
    
    # print(final_str)
    return int(final_str)
    

def main():
    banks = parse_data("input.txt")

    total = 0
    for bank in banks:
        max_joltage = extract_max_joltage(bank, 12)
        total += max_joltage

    print("Total output joltage: ", total)


if __name__ == "__main__":
    main()