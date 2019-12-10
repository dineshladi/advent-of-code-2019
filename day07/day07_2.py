import itertools

def parse_opcode(num):
    op_code = num % 100
    param1 = (num // 100) % 10
    param2 = (num // 1000) % 10
    param3 = (num // 10000) % 10

    return([op_code, param1, param2, param3])


# 0 == position mode, 1 == immediate mode

class Amplifier:
    def __init__(self, data):
        self.data = data[:]
        self.inputs = []
        self.done = False
        self.idx = 0
        self.output = None

    def runProgram(self, user_input):
        self.inputs.append(user_input)
        while True:
            op_code, param1, param2, param3 = parse_opcode(self.data[self.idx])
            if op_code == 1:
                value_1 = self.data[self.data[self.idx + 1]] if param1 == 0 else self.data[self.idx + 1]
                value_2 = self.data[self.data[self.idx + 2]] if param2 == 0 else self.data[self.idx + 2]
                self.data[self.data[self.idx + 3]] = value_1 + value_2
                self.idx = self.idx + 4
            elif op_code == 2:
                value_1 = self.data[self.data[self.idx + 1]] if param1 == 0 else self.data[self.idx + 1]
                value_2 = self.data[self.data[self.idx + 2]] if param2 == 0 else self.data[self.idx + 2]
                self.data[self.data[self.idx + 3]] = value_1 * value_2
                self.idx = self.idx + 4
            elif op_code == 3:
                self.data[self.data[self.idx + 1]] = self.inputs.pop(0)
                self.idx = self.idx + 2
            elif op_code == 4:
                if param1 == 0:
                    self.output = self.data[self.data[self.idx + 1]]
                else:
                    self.output = self.data[self.idx + 1]
                self.idx = self.idx + 2
                return self.output
            elif op_code == 5:
                value_1 = self.data[self.data[self.idx + 1]] if param1 == 0 else self.data[self.idx + 1]
                value_2 = self.data[self.data[self.idx + 2]] if param2 == 0 else self.data[self.idx + 2]
                if value_1 != 0:
                    self.idx = value_2
                else:
                    self.idx = self.idx + 3
            elif op_code == 6:
                value_1 = self.data[self.data[self.idx + 1]] if param1 == 0 else self.data[self.idx + 1]
                value_2 = self.data[self.data[self.idx + 2]] if param2 == 0 else self.data[self.idx + 2]
                if value_1 == 0:
                    self.idx = value_2
                else:
                    self.idx = self.idx + 3
            elif op_code == 7:
                value_1 = self.data[self.data[self.idx + 1]] if param1 == 0 else self.data[self.idx + 1]
                value_2 = self.data[self.data[self.idx + 2]] if param2 == 0 else self.data[self.idx + 2]
                if value_1 < value_2:
                    self.data[self.data[self.idx + 3]] = 1
                else:
                    self.data[self.data[self.idx + 3]] = 0
                self.idx = self.idx + 4
            elif op_code == 8:
                value_1 = self.data[self.data[self.idx + 1]] if param1 == 0 else self.data[self.idx + 1]
                value_2 = self.data[self.data[self.idx + 2]] if param2 == 0 else self.data[self.idx + 2]
                if value_1 == value_2:
                    self.data[self.data[self.idx + 3]] = 1
                else:
                    self.data[self.data[self.idx + 3]] = 0
                self.idx = self.idx + 4
            elif op_code == 99:
                self.done = True
                return self.output


def runAmplifiers(Input, PhaseSettings):
    final_output = 0
    for phase in PhaseSettings:
        amp = Amplifier(Input[:])
        amp.inputs.append(phase)
        final_output = amp.runProgram(final_output)
    return(final_output)


def runAmplifiers_feedback(Input, PhaseSettings):
    amps = [Amplifier(Input[:]) for _ in range(5)]
    final_output = 0
    for amp, phase_setting in zip(amps, PhaseSettings):
        amp.inputs.append(phase_setting)
    while amps[-1].done is False:
        for amp in amps:
            final_output = amp.runProgram(final_output)
    return(final_output)


assert runAmplifiers([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],  [4,  3,  2,  1,  0]) == 43210
assert runAmplifiers([3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0],  [0,  1,  2,  3,  4]) == 54321
assert runAmplifiers([3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0],  [1,  0,  4,  3,  2]) == 65210


RAW = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
PhaseSettings = [9, 8, 7, 6, 5]

assert runAmplifiers_feedback(RAW, PhaseSettings) == 139629729

with open('raw.txt') as file:
    RAW = file.read().split(",")
    RAW = [int(x) for x in RAW]
    print(max([runAmplifiers_feedback(RAW[:], permutation) for permutation in itertools.permutations([9, 8, 7, 6, 5])]))