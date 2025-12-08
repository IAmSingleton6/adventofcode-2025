import math

class Coordinate:
    def __init__(self, x: int, y: int, z: int):
        self._x = x
        self._y = y
        self._z = z
    
    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y
    @property
    def z(self) -> int:
        return self._z

    def get(self) -> tuple[int, int, int]:
        return (self._x, self._y, self._z)

    def distance(self, other: "Coordinate") -> float:
        dx = self._x - other._x
        dy = self._y - other._y
        dz = self._z - other._z
        return math.sqrt(dx*dx + dy*dy + dz*dz)


class JunctionBox:
    def __init__(self, coordinate: Coordinate):
        self.coordinate = coordinate
        self.circuit: Circuit | None = None
    
    def assign_circuit(self, circuit: 'Circuit') -> None:
        self.circuit = circuit


class Circuit:
    def __init__(self):
        self.junction_boxes: list[JunctionBox] = []
    
    def add_junction_box(self, junction_box: JunctionBox) -> None:
        self.junction_boxes.append(junction_box)
        junction_box.assign_circuit(self)
    
    def contains_junction_box_at(self, junction_box: JunctionBox) -> bool:
        return any(
            jb.coordinate.get() == junction_box.coordinate.get()
            for jb in self.junction_boxes
        )
    
    def count_junction_boxes(self) -> int:
        return len(self.junction_boxes)
    
    def merge_circuit(self, circuit: 'Circuit') -> None:
        for jb in circuit.junction_boxes:
            self.add_junction_box(jb)
        circuit.junction_boxes.clear()
    

def parse_data(path: str) -> list[JunctionBox]:
    with open(path) as f:
        lines = f.read().splitlines()
        return [JunctionBox(Coordinate(*map(int, line.split(',')))) for line in lines]

def get_distance_pairs(junction_boxes: list[JunctionBox]) -> list[tuple[JunctionBox, JunctionBox]]:
    pairs: list[tuple[int, JunctionBox, JunctionBox]] = []
    n = len(junction_boxes)
    
    for i in range(n):
        for j in range(i + 1, n):
            c1 = junction_boxes[i].coordinate
            c2 = junction_boxes[j].coordinate
            dist = c1.distance(c2)
            pairs.append((dist, junction_boxes[i], junction_boxes[j]))

    pairs.sort(key=lambda x: x[0])

    return [(box1, box2) for _, box1, box2 in pairs]

def link_junction_boxes(junction_boxes: list[JunctionBox], iterations: int) -> list[Circuit]:
    circuits: list[Circuit] = []
    distance_pairs = get_distance_pairs(junction_boxes)

    for iteration in range(iterations):
        jb1, jb2 = distance_pairs[iteration]
        if jb1.circuit is None and jb2.circuit is None:
            circuit = Circuit()
            circuit.add_junction_box(jb1)
            circuit.add_junction_box(jb2)
            circuits.append(circuit)
        
        elif jb1.circuit is not None and jb2.circuit is None:
            jb1.circuit.add_junction_box(jb2)

        elif jb1.circuit is None and jb2.circuit is not None:
            jb2.circuit.add_junction_box(jb1)

        elif jb1.circuit is not jb2.circuit:
            circuits.remove(jb2.circuit)
            jb1.circuit.merge_circuit(jb2.circuit)

    return [circuit for circuit in circuits if circuit.count_junction_boxes() > 0]

def main():
    junction_boxes = parse_data("input.txt")

    circuits = link_junction_boxes(junction_boxes, 1000)
    circuit_sizes = [circuit.count_junction_boxes() for circuit in circuits]
    circuit_sizes.sort(reverse=True)

    print("Top 3 product: ", circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2])

if __name__ == "__main__":
    main()