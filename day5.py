from copy import deepcopy

with open("inputs/input_day5.txt") as file:
    inputs = [[[int(x)
                for x in point.split(',')]
               for point in line.split(' -> ')]
              for line in file.read().split('\n')[:-1]]
all_points = set()
all_points1 = set()

c = 0
for line in inputs:
    a, b = line
    x1, y1 = a
    x2, y2 = b

    xl = list(range(min(x1, x2), max(x1, x2)+1))
    yl = list(range(min(y1, y2), max(y1, y2)+1))
    if len(xl) > 1 and len(yl) > 1:
        continue
    for xs in xl:
        for ys in yl:
            if (xs, ys) in all_points and (xs, ys) not in all_points1:
                c += 1
                all_points1.add((xs, ys))
            elif (xs, ys) not in all_points:
                all_points.add((xs, ys))

print(c)

all_points = set()
all_points1 = set()

c = 0
for line in inputs:
    a, b = line
    x1, y1 = a
    x2, y2 = b

    xl = list(range(min(x1, x2), max(x1, x2)+1))
    yl = list(range(min(y1, y2), max(y1, y2)+1))
    if x1 > x2:
        xl.reverse()
    if y1 > y2:
        yl.reverse()
    # print(xl, yl)
    if 1 < len(xl) == len(yl) > 1:
        for xs, ys in zip(xl, yl):
            if (xs, ys) in all_points and (xs, ys) not in all_points1:
                c += 1
                all_points1.add((xs, ys))
            elif (xs, ys) not in all_points:
                all_points.add((xs, ys))
    else:
        for xs in xl:
            for ys in yl:
                if (xs, ys) in all_points and (xs, ys) not in all_points1:
                    c += 1
                    all_points1.add((xs, ys))
                elif (xs, ys) not in all_points:
                    all_points.add((xs, ys))

print(c)
