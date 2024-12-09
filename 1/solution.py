import sys

lines = [l.strip() for l in sys.stdin.readlines()]
group_one = sorted([int(line[:5]) for line in lines])
group_two = sorted([int(line[8:]) for line in lines])
print("Part One: ", sum([abs(group_one[i] - group_two[i]) for i in range(len(lines))]))
print("Part Two: ", sum([group_two.count(v) * v for v in group_one]))
