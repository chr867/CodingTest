import sys
sys.setrecursionlimit(10 ** 6) # 재귀 한도

# N(N-1) / 2 인접행렬
N, M = map(int, sys.stdin.readline().strip().split())
adj = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: x -1, map(int, sys.stdin.readline().strip().split()))
    adj[a][b] = adj[b][a] = 1

ans = 0
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)