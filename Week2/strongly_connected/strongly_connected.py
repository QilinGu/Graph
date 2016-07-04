#Uses python3

import sys

sys.setrecursionlimit(200000)


def post_explore(x, adj, visited, post_order):
    visited[x] = True
    for each in adj[x]:
        if not visited[each]:
            post_explore(each, adj, visited, post_order)
    post_order.append(x)


def reverse_graph(adj):
    new_adj = [[] for i in range(len(adj))]
    for i, each in enumerate(adj):
        for e in each:
            new_adj[e].append(i)
    return new_adj

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


def number_of_strongly_connected_components(adj):
    result = 0
    graph = dfs(reverse_graph(adj))
    graph.reverse()
    visited = [False] * len(adj)
    for each in graph:
        if not visited[each]:
            scc = []
            explore(each, adj, scc, visited)
            result += 1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
#7 1 3 8 4 5 9 2 6 10