import sys
import re

def is_enabled(instr, index):
    return instr[max(0, next((i for i in range(len(instr)) if instr[i][0] > index), len(instr)) - 1)][1] == "on"

text = sys.stdin.read()
dos = [(m.start(), "on") for m in re.finditer(r'do\(\)', text)]
donts = [(m.start(), "off") for m in re.finditer(r'don\'t\(\)', text)]
instructions = sorted(dos + donts)
matches_iter = re.finditer(r'mul\((\d+),(\d+)\)', text)
# matches = list(matches_iter)
# print("Part 1: ", sum([int(m.groups(0)[0]) * int(m.groups(0)[1]) for m in matches]))
print("Part 2: ", sum([(int(m.groups(0)[0]) * int(m.groups(0)[1]) if is_enabled(instructions, m.start()) else 0) for m in matches_iter]))