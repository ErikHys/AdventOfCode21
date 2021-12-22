from copy import deepcopy

with open("inputs/input_day3.txt") as file:
    inputs = [x for x in file.read().split('\n')[:-1]]


# part 1
def binary_to_decimal(v):
    return int(v, 2)


def get_gamma_epsilon(binaries):
    epsilon = ""
    gamma = ""
    # should do this simply with an list comprehension and nd array
    new_binaries = []
    for i in range(len(binaries[0])):
        binary = [x[i] for x in binaries]
        new_binaries.append(binary)

    for binary in new_binaries:
        if binary.count('1') < binary.count('0'):
            gamma = gamma + '0'
            epsilon = epsilon + '1'
        else:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
    return gamma, epsilon


#gamma, epsilon = get_gamma_epsilon(inputs)
#print(binary_to_decimal(gamma)*binary_to_decimal(epsilon))


# part 2

def transpose(binaries):
    if not binaries:
        return []
    new_binaries = []
    for i in range(len(binaries[0])):
        binary = [x[i] for x in binaries]
        new_binaries.append(binary)
    return new_binaries


def get_o2(binaries):
    # should do this simply with an list comprehension and nd array
    new_binaries = transpose(binaries)
    result = ""
    for i in range(len(binaries[0])):
        binary = new_binaries[i]
        if binary.count('1') >= binary.count('0'):
            result = result + '1'
            for j in range(len(binary)-1, -1, -1):
                v = binary[j]
                if v == '0':
                    binaries.pop(j)
        else:
            result = result + '0'
            for j in range(len(binary)-1, -1, -1):
                v = binary[j]
                if v == '1':
                    binaries.pop(j)
        new_binaries = transpose(binaries)
    return result


def get_co2(binaries):
    # should do this simply with an list comprehension and nd array
    new_binaries = transpose(binaries)
    result = ""
    for i in range(len(binaries[0])):
        binary = new_binaries[i]
        if len(binaries) == 1:
            result = result + binaries[0][i:]
            break
        if binary.count('1') < binary.count('0'):
            result = result + '1'
            for j in range(len(binary)-1, -1, -1):
                v = binary[j]
                if v == '0':
                    binaries.pop(j)
        else:
            result = result + '0'
            for j in range(len(binary)-1, -1, -1):
                v = binary[j]
                if v == '1':
                    binaries.pop(j)
        new_binaries = transpose(binaries)
    return result


o2 = get_o2(deepcopy(inputs))
co2 = get_co2(deepcopy(inputs))
print(binary_to_decimal(o2)*binary_to_decimal(co2))

