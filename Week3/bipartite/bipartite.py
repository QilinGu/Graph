#Uses python3

import sys
from collections import deque

def bipartite(adj):
    #write your code here
    d = [-1] * len(adj)
    d[0] = 0
    Q = deque()
    Q.append(0)
    while Q:
        u = Q.pop()
        for each in adj[u]:
            if d[each] == -1:
                d[each] = d[u] + 1
                Q.append(each)
            elif d[each] % 2 == d[u] % 2:
                return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
