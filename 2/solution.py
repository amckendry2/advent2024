import sys
import math

def check_range(diffs):
    return all(max(0, min(abs(val), 3)) == abs(val) for val in diffs)

def check_dir(diffs):
    dir = math.copysign(1, diffs[0])
    return all(v != 0 and math.copysign(1, v) == dir for v in diffs)

def is_safe(line):
    diffs = [line[i] - line[i-1] for i in range(len(line))[1:]]
    return check_range(diffs) and check_dir(diffs)

def try_safe(line):
    return any(is_safe(line[:i] + line[i+1:]) for i in range(len(line)))

lines = [[int(n) for n in line.strip().split(' ')] for line in sys.stdin.readlines()]
print("Part 1: ", sum([is_safe(line) for line in lines]))
print("Part 2: ", sum([is_safe(line) or try_safe(line) for line in lines]))
