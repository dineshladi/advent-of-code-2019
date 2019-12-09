
def do_the_operation(lst, noun, verb):
    data = lst.copy()
    # Resote gravity assit program
    data[1] = noun
    data[2] = verb

    for idx in range(0, len(raw), 4):
        if (data[idx] == 1):
            data[data[idx+3]] = data[data[idx+1]] + data[data[idx+2]]
        elif (data[idx] == 2):
            data[data[idx+3]] = data[data[idx+1]] * data[data[idx+2]]
        elif (data[idx] == 99):
            break
        else:
            continue
    return(data[0])


with open('raw.txt') as file:
    raw = file.read().split(",")
    raw = list(map(int, raw))

    print(do_the_operation(raw, 12, 2))

    # 2nd part

    for noun in range(0, 99):
        for ver in range(0, 99):
            result = do_the_operation(raw, noun, ver)
            if(result == 19690720):
                print((100 * noun) + ver)
                break
