class Safe:
    def __init__(self, start = 50):
        self._count = start

    @property
    def count(self):
        return self._count
    
    def right_turn(self, amount: int) -> bool:
        temp = self._count + amount
        temp = temp % 100
        self._count = temp
        return self.is_zero()
        
    
    def left_turn(self, amount: int) -> bool:
        temp = self._count - amount
        temp = temp % 100
        self._count = temp
        return self.is_zero()
    
    def is_zero(self) -> bool:
        return self._count == 0


def parse_turns(path="input.txt") -> list[str]:
    with open(path) as f:
        return [line.strip() for line in f]


def count_turns(turns, safe):
    handlers = {
        "R": safe.right_turn,
        "L": safe.left_turn,
    }

    return sum(
        handlers[turn[0]](int(turn[1:]))       
        for turn in turns
        if turn[0] in handlers            
    )


def main():
    safe = Safe(50)
    
    turns = parse_turns("input.txt")
    x = count_turns(turns, safe)
    print(x)



if __name__ == "__main__":
    main()