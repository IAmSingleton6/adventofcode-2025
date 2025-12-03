def parse_data(path: str) -> list[str]:
    with open(path) as f:
        return f.read().splitlines()


def extract_max_joltage(bank: str) -> int:
    starting_digit = -1
    starting_index = -1

    # Loop through all except the last
    for i, joltage in enumerate(bank[:-1]):
        digit = int(joltage)
        if digit > starting_digit:
            starting_digit = digit
            starting_index = i
    
    final_digit = -1
    for joltage in bank[starting_index + 1:]:
        digit = int(joltage)
        final_digit = max(digit, final_digit)
    
    max_joltage_str = str(starting_digit) + str(final_digit)
    return int(max_joltage_str)
    

def main():
    banks = parse_data("input.txt")

    total = 0
    for bank in banks:
        max_joltage = extract_max_joltage(bank)
        total += max_joltage

    print("Total output joltage: ", total)


if __name__ == "__main__":
    main()