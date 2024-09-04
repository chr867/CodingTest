import heapq
import sys

heap_list = []
for i in range(int(sys.stdin.readline().strip())):
    num = int(sys.stdin.readline().strip())
    if num != 0:
        heapq.heappush(heap_list, (abs(num), num))
    elif len(heap_list) != 0:
        print(heap_list[0][1])
        heapq.heappop(heap_list)
    else:
        print(0)
