from itertools import combinations
import sys
height_list = []
for i in range(9):
    height_list.append(int(sys.stdin.readline().strip()))

com = combinations(height_list, 7)

for i in com:
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break    