
def parse_instruction(num):
    op_code = num % 100
    param1 = (num // 100) % 10
    param2 = (num // 1000) % 10
    param3 = (num // 10000) % 10

    return([op_code, param1, param2, param3])


# 0 == position mode, 1 == immediate mode


def do_the_operation(RAW, user_input):
    data = RAW[:]
    output = []
    idx = 0
    while data[idx] != 99:
        op_code, param1, param2, param3 = parse_instruction(data[idx])
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
            value = data[data[idx+1]] if param1 == 0 else data[idx+1]
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


with open('raw.txt') as file:
    RAW = file.read().split(",")
    RAW = [int(x) for x in RAW]
    print(do_the_operation(RAW, [1]))
    print(do_the_operation(RAW, [5]))
