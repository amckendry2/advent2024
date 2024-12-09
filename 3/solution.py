import sys
import re

def is_enabled(instr, index):
    idx = next((i for i in range(len(instr)) if instr[i][0] > index), len(instr)) - 1
    return True if idx == -1 else instr[max(0, idx)][1] == "on"

text = sys.stdin.read()
instructions = sorted([(m.start(), "on") for m in re.finditer(r'do\(\)', text)] +
                      [(m.start(), "off") for m in re.finditer(r'don\'t\(\)', text)])
mults = [(m.start(), m) for m in re.finditer(r'mul\((\d+),(\d+)\)', text)]
print("Part 1: ", sum([int(m[1].groups(0)[0]) * int(m[1].groups(0)[1]) for m in mults]))
print("Part 2: ", sum([int(m[1].groups(0)[0]) * int(m[1].groups(0)[1]) if is_enabled(instructions, m[0]) else 0 for m in mults]))