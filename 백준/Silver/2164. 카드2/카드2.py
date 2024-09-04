from collections import deque
deque = deque()

for i in range(int(input())):
    deque.append(i+1)

while len(deque) > 1:
    deque.popleft()
    deque.append(deque.popleft())

print(deque[0])