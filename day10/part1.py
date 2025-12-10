import itertools
import re

IndicatorLight = bool
IndicatorLights = list[bool]
Joltage = int
Button = set[int]

class Machine:
    def __init__(
            self, 
            expected_lights: IndicatorLights, 
            buttons: list[Button], 
            joltages: list[Joltage]):
        
        self.expected_lights = expected_lights
        self.buttons = buttons
        self.joltages = joltages

class Parser:
    def parse_data(self, path: str) -> list[Machine]:
        machines = []
        light_map = {
            '#': True,
            '.': False
        }
        with open(path) as f:
            lines = f.read().splitlines()
            for line in lines:
                indicator_lights = [IndicatorLight(light_map[l]) for l in self.find_all_inside(line, '[', ']')[0]]
                buttons = [set(map(int, b.split(','))) for b in self.find_all_inside(line, '(', ')')]
                joltages = [Joltage(j) for j in self.find_all_inside(line, '{', '}')[0].split(',')]
                machine = Machine(indicator_lights, buttons, joltages)
                machines.append(machine)

        return machines

    def find_all_inside(self, text: str, left: chr, right: chr) -> list[str]:
        pattern = re.escape(left) + r'(.*?)' + re.escape(right)
        return re.findall(pattern, text)


def solve(machine: Machine):
    expected = machine.expected_lights
    buttons = machine.buttons
    n = len(expected)
    k = len(buttons)

    # Try 0 presses, 1 press, 2 presses, ...
    for press_count in range(k + 1):
        for combo in itertools.combinations(range(k), press_count):
            lights = [False] * n

            for btn_index in combo:
                flip_states(lights, buttons[btn_index])
            
            if lights == expected:
                return press_count

    return None  

def flip_states(lights: IndicatorLights, button: Button):
    for light in button:
        lights[light] = not lights[light]

def main():
    machines = Parser().parse_data("input.txt")
    result = sum(solve(machine) for machine in machines)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()