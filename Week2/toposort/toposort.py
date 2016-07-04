#Uses python3

import sys



def dfs(x, adj, visited, post_order):
    visited[x] = True
    for each in adj[x]:
        if not visited[each]:
            dfs(each, adj, visited, post_order)
    post_order.append(x)


def toposort(adj):
    post_order = []
    visited = [False] * len(adj)
    for i, each in enumerate(visited):
        if not each:
            dfs(i, adj, visited, post_order)
    post_order.reverse()
    return post_order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

