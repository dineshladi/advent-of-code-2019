

raw = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L'''


def make_dict(string):
    raw = string.strip().split("\n")
    pairs = {}
    for x in raw:
        parent, child = x.split(")")
        pairs[child] = parent
    return(pairs)


def count_parents(string, child):
    records = make_dict(string)
    count = 0
    while child != 'COM':
        count += 1
        child = records[child]
    return(count)


def get_ancestors(string, child):
    records = make_dict(string)
    ancestors = []
    while child != 'COM':
        ancestors.append(child)
        child = records[child]
    return(ancestors)


def count_total_orbits(string):
    pairs = make_dict(string)
    return(sum([count_parents(string, x) for x in pairs.keys()]))


assert count_parents(raw, "L") == 7
assert count_parents(raw, "D") == 3
assert count_total_orbits(raw) == 42


# 2nd part
def common_ancestors(string, sat1, sat2):
    a1 = get_ancestors(string, sat1)
    a2 = get_ancestors(string, sat2)
    return(set(a1).intersection(set(a2)))


def count_till_an_orbit(string, sat, dest):
    ances = get_ancestors(string, sat)
    count = 0
    for i in ances:
        count += 1
        if i == dest:
            break
    return(count)


def min_transfers(string, sat1, sat2):
    records = make_dict(string)
    orbit1 = records[sat1]
    orbit2 = records[sat2]
    common = common_ancestors(string, orbit1, orbit2)
    return(min([count_till_an_orbit(string, sat1, x) +
           count_till_an_orbit(string, sat2, x) for x in common]) - 4)


RAW = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""


assert min_transfers(RAW, "SAN", "YOU") == 4

with open('raw.txt') as file:
    data = file.read()
    print(count_total_orbits(data))
    print(min_transfers(data, "SAN", "YOU"))