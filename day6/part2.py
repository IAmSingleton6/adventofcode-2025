class MathProblem:
    def __init__(self, operator: str, numbers: list[int] = None):
        self.numbers = numbers if numbers is not None else []
        self.operator = operator
    
    def add_number(self, number: int) -> None:
        self.numbers.append(number)

    def add_operator(self, operator: str) -> None:
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


class MathProblemParser:
    def __init__(self, rows: list[str]):
        self.rows = rows
        self.row_size = len(rows[0])
        self.col_size = len(rows)
        self.pointer = 0
    
    def parse(self) -> list[MathProblem]:
        math_problems: list[MathProblem] = []

        while self.pointer < self.row_size:
            math_problems.append(self.parse_chunk())

        return math_problems

    def is_skip_column(self) -> bool:
        if self.pointer >= len(self.rows[0]):
            return True

        for row in self.rows:
            if row[self.pointer] != " ":
                return False
        return True
    
    def parse_chunk(self) -> MathProblem:
        op = self.rows[-1][self.pointer]
        nums = []

        while not self.is_skip_column():
            num = ""
            for row in self.rows[:-1]:
                num += row[self.pointer]
            nums.append(int(num.strip()))

            self.pointer += 1
        
        self.pointer += 1  
        return MathProblem(operator=op, numbers=nums)


def parse_data(path: str) -> list[MathProblem]:
    with open(path) as f:
        rows = f.read().splitlines()
        return MathProblemParser(rows).parse()

def main():
    math_problems = parse_data("input.txt")
    total = sum(problem.solve() for problem in math_problems)
    print("Total sum of all problems:", total)

if __name__ == "__main__":
    main()