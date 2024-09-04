# K원을 만들기 위해 N개의 동전 종류를 활용
import sys
from math import floor

coins = []
T = sys.stdin.readline().strip().split(" ")
N = int(T[0])
K = int(T[1])
for i in range(N):
    coins.append(int(sys.stdin.readline().strip()))

coins.reverse()
count = 0
for i in coins:
    if K / i >= 1:
        count = count + floor(K / i)
        K = K % i
print(count)