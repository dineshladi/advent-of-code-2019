import itertools

def parse_opcode(num):
    op_code = num % 100
    param1 = (num // 100) % 10
    param2 = (num // 1000) % 10
    param3 = (num // 10000) % 10

    return([op_code, param1, param2, param3])


# 0 == position mode, 1 == immediate mode


def runProgram(RAW, user_input):
    data = RAW[:]
    output = []
    idx = 0
    while data[idx] != 99:
        op_code, param1, param2, param3 = parse_opcode(data[idx])
        if op_code == 1:
            value_1 = data[data[idx+1]] if param1 == 0 else data[idx+1]
            value_2 = data[data[idx+2]] if param2 == 0 else data[idx+2]
            data[data[idx+3]] = value_1 + value_2
            idx = idx + 4
        elif op_code == 2:
            value_1 = data[data[idx+1]] if param1 == 0 else data[idx+1]
            value_2 = data[data[idx+2]] if param2 == 0 else data[idx+2]
            data[data[idx+3]] = value_1 * value_2
            idx = idx + 4
        elif op_code == 3:
            input_value = user_input[0]
            user_input = user_input[1:]
            data[data[idx+1]] = input_value
            idx = idx + 2
        elif op_code == 4:
            if param1 == 0:
                value = data[data[idx + 1]]
            else:
                value = data[idx + 1]
            output.append(value)
            idx = idx + 2
        elif op_code == 5:
            value_1 = data[data[idx+1]] if param1 == 0 else data[idx+1]
            value_2 = data[data[idx+2]] if param2 == 0 else data[idx+2]
            if value_1 != 0:
                idx = value_2
            else:
                idx = idx + 3
        elif op_code == 6:
            value_1 = data[data[idx+1]] if param1 == 0 else data[idx+1]
            value_2 = data[data[idx+2]] if param2 == 0 else data[idx+2]
            if value_1 == 0:
                idx = value_2
            else:
                idx = idx + 3
        elif op_code == 7:
            value_1 = data[data[idx+1]] if param1 == 0 else data[idx+1]
            value_2 = data[data[idx+2]] if param2 == 0 else data[idx+2]
            if value_1 < value_2:
                data[data[idx+3]] = 1
            else:
                data[data[idx+3]] = 0
            idx = idx + 4
        elif op_code == 8:
            value_1 = data[data[idx+1]] if param1 == 0 else data[idx+1]
            value_2 = data[data[idx+2]] if param2 == 0 else data[idx+2]
            if value_1 == value_2:
                data[data[idx+3]] = 1
            else:
                data[data[idx+3]] = 0
            idx = idx + 4
        else:
            raise RuntimeError("Bad optcode")
    return(output)


def execute_amplifier(Input, phase, signal):
    output = runProgram(Input, [phase, signal[0]])
    return(output)


def runAmplifiers(Input, PhaseSettings):
    final_output = [0]
    for phase in PhaseSettings:
        final_output = execute_amplifier(Input, phase, final_output)
    return(final_output)


def max_thrust_signal(Input, phase_comb):
    return(max([runAmplifiers(Input, x)[0] for x in itertools.permutations(phase_comb)]))


assert runAmplifiers([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], [4, 3, 2, 1, 0]) == [43210]
assert runAmplifiers([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], [0, 1, 2, 3, 4]) == [54321]
assert runAmplifiers([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], [1, 0, 4, 3, 2]) == [65210]


with open('raw.txt') as file:
    RAW = file.read().split(",")
    RAW = [int(x) for x in RAW]

    lst = [0, 1, 2, 3, 4]
    print(max_thrust_signal(RAW, lst))


