#Uses python3

import sys


def post_explore(x, adj, visited, post_order):
    visited[x] = True
    for each in adj[x]:
        if not visited[each]:
            post_explore(each, adj, visited, post_order)
    post_order.append(x)


def dfs(adj):
    post_order = []
    visited = [False] * len(adj)
    for i, each in enumerate(visited):
        if not each:
            post_explore(i, adj, visited, post_order)
    return post_order


def explore(x, adj, scc, visited):
    visited[x] = True
    scc.append(x)
    for each in adj[x]:
        if not visited[each]:
            explore(each, adj, scc, visited)


def acyclic(adj):
    graph = dfs(adj)
    print(graph)
    visited = [False] * len(adj)
    for each in graph:
        if not visited[each]:
            scc = []
            explore(each, adj, scc, visited)
            if len(scc) > 1:
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
'''
8 9
1 2
3 2
7 2
7 3
4 6
6 3
3 5
7 5
8 5
'''