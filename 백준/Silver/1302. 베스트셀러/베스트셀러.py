# min()
import sys

dic = {}
for i in range(int(sys.stdin.readline().strip())):
    key = sys.stdin.readline().strip()
    if dic.get(key) is None:
        dic[key] = 1
    else:
        dic[key] = dic[key] + 1

maxVal = max(dic.values())
keys = []
for i in dic:
    if dic[i] == maxVal:
        keys.append(i)
print(min(keys))