#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    prev = [-1] * len(distance)
    distance[s] = 0
    prev[s] = s
    nodes_with_cycles = set()
    for i in range(len(adj)):
        for u in range(len(adj)):
            for v_i, v in enumerate(adj[u]):
                if distance[v] > distance[u] + cost[u][v_i]:
                    distance[v] = distance[u] + cost[u][v_i]
                    prev[v] = u
                    if i == len(adj) - 1:
                        nodes_with_cycles.add(v)
    for u in range(len(adj)):
        for v_i, v in enumerate(adj[u]):
            if u in nodes_with_cycles:
                nodes_with_cycles.add(v)
    for i in range(len(prev)):
        if prev[i] != -1:
            reachable[i] = 1
            if i in nodes_with_cycles:
                shortest[i] = 0



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m) :3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

