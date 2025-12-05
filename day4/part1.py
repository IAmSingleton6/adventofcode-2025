PAPER_CHAR = '@'
EMPTY_CHAR = '.'

def parse_data(path: str) -> list[list[str]]:
    with open(path) as f:
        return [list(line) for line in f.read().splitlines()]

def get_neighbouring_paper_count(position: tuple[int, int], data: list[list[str]]):
    x, y = position
    rows = len(data)
    cols = len(data[0])
    
    directions = [
        (-1,  0),  
        (-1,  1),  
        (0,   1),  
        (1,   1),  
        (1,   0),  
        (1,  -1),  
        (0,  -1),  
        (-1, -1),  
    ]
    
    count = 0
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < rows and 0 <= ny < cols:
            if data[nx][ny] == PAPER_CHAR:
                count += 1
    
    return count

def main():
    data = parse_data("input.txt")
    total = 0

    for row_index, row in enumerate(data):
        for col_index, col in enumerate(row):
            if col != PAPER_CHAR:
                continue
            neighbour_count = get_neighbouring_paper_count((row_index, col_index), data)
            if neighbour_count < 4:
                total += 1
        

    print(total)

if __name__ == "__main__":
    main()