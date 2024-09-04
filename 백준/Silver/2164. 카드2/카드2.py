from collections import deque
import sys
deque = deque()

for i in range(int(sys.stdin.readline())):
    deque.append(i+1)

while len(deque) > 1:
    deque.popleft()
    deque.append(deque.popleft())

print(deque[0])