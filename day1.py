with open("inputs/input_day_1.txt") as file:
    depths = [int(x) for x in file.read().split('\n')[:-1]]

# depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
# part 1
c = 0
for i in range(1, len(depths)):
    if depths[i-1] < depths[i]:
        c += 1
print(c)

# part 2

c = 0
for i in range(3, len(depths)):
    if sum(depths[i-3:i]) < sum(depths[i-2:i+1]):
        # print(sum(depths[i - 4:i - 1]), sum(depths[i - 3:i]), "passed")
        c += 1
    else:
        # print(sum(depths[i - 4:i - 1]), sum(depths[i - 3:i]), "failed")
        pass

print(c)