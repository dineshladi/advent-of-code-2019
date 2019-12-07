
# part 1


def fuel_required(mass):
    return (mass//3) - 2


with open('raw.txt') as file:
    lines = file.read().split("\n")
    print(sum([fuel_required(int(x)) for x in lines]))

def recursive_fuel(fuel):
    total_fuel = 0
    while fuel >= 0:
        fuel = fuel_required(fuel)
        if(fuel <= 0):
            break
        total_fuel = total_fuel + fuel
    return(total_fuel)

with open('raw.txt') as file:
    lines = file.read().split("\n")
    print(sum([recursive_fuel(int(x)) for x in lines]))

assert recursive_fuel(14) == 2
assert recursive_fuel(1969) == 966
assert recursive_fuel(100756) == 50346

