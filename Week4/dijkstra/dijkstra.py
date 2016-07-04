#Uses python3

import sys
import heapq


def distance(adj, cost, s, t):
    #write your code here
    dist = [sys.maxsize] * len(adj)
    dist[s] = 0
    H = []
    for i in range(len(adj)):
        heapq.heappush(H, (dist[i], i))
    while H:
        u = heapq.heappop(H)[1]
        for v in adj[u]:
            if dist[v] > dist[u] + cost[u][v]:
                dist[v] = dist[u] + cost[u][v]
                heapq.heappush(H, (dist[v],v))
    if dist[t] == sys.maxsize:
        return -1
    return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[None] * n for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1][b-1] = w
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
