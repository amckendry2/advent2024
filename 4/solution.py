import sys
import re

h_lines = [l.strip() for l in sys.stdin.readlines()]
w = len(h_lines[0])
v_lines = [''.join([l[i] for l in h_lines]) for i in range(w)]
l_diag_lines = [''.join([l[i - li] if i - li >= 0 and i - li < w else 'O' for li, l in enumerate(h_lines)]) for i in range(w * 2 - 1)]
r_diag_lines = [''.join([l[i + li] if i + li >= 0 and i + li < w else 'O' for li, l in enumerate(h_lines)]) for i in range(w - 1, -w, -1)]
print("Part 1: ", sum([l.count("XMAS") + l.count("SAMX") for l in h_lines + v_lines + l_diag_lines + r_diag_lines]))
count = 0
for li, l in enumerate(l_diag_lines):
    idxs = [m.start() for m in re.finditer('(?=SAM|MAS)', l)]
    for i in idxs:
        r_sample = r_diag_lines[(w - 1) - (li - 2 * (i + 1))][i:i + 3]
        if r_sample == "SAM" or r_sample == "MAS":
            count += 1
print("Part 2: ", count)
