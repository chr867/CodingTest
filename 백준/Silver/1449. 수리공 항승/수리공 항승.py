## 첫째 줄 -> 물이 새는 곳의 개수 N, 테이프의 길이 L
# 둘째 줄 -> 물이 새는 곳의 위치
# 가장 왼쪽에서 정수만큼 떨어진 거리에서 물이 새고 좌우 0.5의 간격을 줘야함
# 정수 + (테이프 길이 - 0.5) 범위 안에 든다면 테이프를 사용하지 않는다.
# #
import sys
N, L = map(int, sys.stdin.readline().strip().split())
repair = list(map(int, sys.stdin.readline().strip().split()))
repair.sort()
ans = 0
fixed_range = 0
for i in repair:
    if i >= fixed_range:
        ans += 1
        fixed_range = i + (L - 0.5)
print(ans)