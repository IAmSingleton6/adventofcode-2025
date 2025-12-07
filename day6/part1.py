class MathProblem:
    def __init__(self, operator: str, numbers: list[int] = None):
        self.numbers = numbers if numbers is not None else []
        self.operator = operator
    
    def add_number(self, number: int) -> None:
        self.numbers.append(number)

    def set_operator_operator(self, operator: str) -> None:
        self.operator = operator
    
    def solve(self) -> int:
        if self.operator == "+":
            return sum(self.numbers)
        elif self.operator == "*":
            result = 1
            for num in self.numbers:
                result *= num
            return result
        else:
            raise ValueError("Unsupported operator")


def parse_data(path: str) -> list[MathProblem]:
    with open(path) as f:
        rows = f.read().splitlines()
        operators = parse_operators(rows[-1])
        math_problems = [MathProblem(operator=op) for op in operators]

        for row in rows[:-1]:
            numbers = parse_numbers(row)
            for i, num in enumerate(numbers):
                math_problems[i].add_number(int(num))
    
    return math_problems

def parse_numbers(row: str) -> list[str]:
    return row.split()

def parse_operators(row: str) -> list[str]:
    ops = "+*"
    operators = [ch for ch in row if ch in ops]
    return operators

def main():
    math_problems = parse_data("input.txt")
    total = sum(problem.solve() for problem in math_problems)
    print("Total sum of all problems:", total)

if __name__ == "__main__":
    main()