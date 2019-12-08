
def traverse(path):
    steps = path.split(",")
    steps = [[step[0:1], int(step[1:])] for step in steps]
    x = 0
    y = 0
    points = []
    for direction, dist in steps:
        for _ in range(dist):
            if direction == 'R':
                x = x + 1
            elif direction == 'L':
                x = x - 1
            elif direction == 'U':
                y = y + 1
            elif direction == 'D':
                y = y - 1
            else:
                raise RuntimeError("Bad directional input")

            points.append((x, y))

    return(points)


def compute_intersection(line1, line2):
    line1_points = traverse(line1)
    line2_points = traverse(line2)

    return(set(line2_points) & set(line1_points))


def lowest_manhattan(line1, line2):
    intersected = compute_intersection(line1, line2)

    return(min([abs(x[0]) + abs(x[1]) for x in intersected]))


line1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
line2 = "U62,R66,U55,R34,D71,R55,D58,R83"
assert lowest_manhattan(line1, line2) == 159

line1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
line2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
assert lowest_manhattan(line1, line2) == 135


with open('raw.txt') as file:
    line1, line2 = file.readlines()
    print(lowest_manhattan(line1, line2))