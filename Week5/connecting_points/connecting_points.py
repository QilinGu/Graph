#Uses python3
import sys
import math
import heapq


def get_id(x):
    global parent
    if x != parent[x]:
        parent[x] = get_id(parent[x])
    return parent[x]


def join(x, y):
    global parent, rank
    first_id, second_id = get_id(x), get_id(y)
    if rank[first_id] >= rank[second_id]:
        parent[second_id] = first_id
        rank[first_id] += 1
    else:
        parent[first_id] = second_id
        rank[second_id] += 1


def minimum_distance(x, y):
    result = 0.
    #write your code here
    weights = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if i != j:
                heapq.heappush(weights, (math.sqrt((x[i] - x[j])**2+(y[i] - y[j])**2), i, j))
    while weights:
        distance, x, y = heapq.heappop(weights)
        if get_id(x) != get_id(y):
            result += distance
            join(x, y)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    rank = [1 for i in range(n)]
    parent = [i for i in range(n)]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
