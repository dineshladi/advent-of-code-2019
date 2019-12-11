import numpy as np
dim = [25, 6]
with open('raw.txt') as file:
    RAW = file.read()

Layers = int(len(RAW)/(dim[0]*dim[1]))
pixels = [RAW[layer*dim[0]*dim[1]: (layer + 1)*dim[0]*dim[1]] for layer in range(Layers)]
pixels = [[int(x) for x in layer] for layer in pixels]

zero_counts = [sum([x == 0 for x in layer]) for layer in pixels]


min_zero_index = zero_counts.index(min(zero_counts))


print(sum([x == 1 for x in pixels[min_zero_index]])*sum([x == 2 for x in pixels[min_zero_index]]))


# part 2
dim = [25, 6]
with open('raw.txt') as file:
    RAW = file.read()

#RAW = "0222112222120000"
Layers = int(len(RAW)/(dim[0]*dim[1]))
#print(Layers)
pixels = [RAW[layer*dim[0]*dim[1]: (layer + 1)*dim[0]*dim[1]] for layer in range(Layers)]
pixels = [[int(x) for x in layer] for layer in pixels]

message = []
for pos in range(dim[0]*dim[1]):
    visible = pixels[0][pos]
    for layer in pixels:
        if layer[pos] != 2 and visible in [0,1]:
            break
        elif layer[pos] in [0,1]:
            visible = layer[pos]
            break
    message.append(visible)
print(len(message))
print(message)
message = "".join([str(x) for x in message])
message = message.replace("0", " ")
message = message.replace("1",c"#")
print(message)

width = 25
height = 6

for h in range(height):
    print(" ".join([x for x in message[h*width:(h+1)*width]]))