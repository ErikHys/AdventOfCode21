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


gamma, epsilon = get_gamma_epsilon(inputs)
print(binary_to_decimal(gamma)*binary_to_decimal(epsilon))


# part 2
import numpy as np


def get_o2(binaries):
    # should do this simply with an list comprehension and nd array
    new_binaries = []
    for i in range(len(binaries[0])):
        binary = np.array([x[i] for x in binaries])
        new_binaries.append(binary)
    new_binaries = np.array(new_binaries)


