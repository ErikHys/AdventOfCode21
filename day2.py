with open("inputs/input_day2.txt") as file:
    inputs = [(x.split()[0], int(x.split()[1])) for x in file.read().split('\n')[:-1]]

# inputs = [("forward", 5), ("down", 5), ("forward", 8), ("up", 3),
#           ("down", 8), ("forward", 2)]

# part 1
h = 0
v = 0
for dir, val in inputs:
    if dir == "forward":
        h += val
    elif dir == "down":
        v += val
    elif dir == "up":
        v -= val

print(h, v)
print(h*v)

# part 2

h = 0
v = 0
a = 0
for dir, val in inputs:
    if dir == "forward":
        h += val
        v += val*a
    elif dir == "down":
        a += val
    elif dir == "up":
        a -= val

print(h, v, a)
print(h*v)