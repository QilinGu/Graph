#Uses python3
import sys
import math
import heapq
import decimal


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
        return first_id
    else:
        parent[first_id] = second_id
        rank[second_id] += 1
        return second_id


def clustering(x_, y_, k):
    #write your code here
    result = 0
    # write your code here
    weights = []
    sets = set([i for i in range(len(x_))])
    for i in range(len(x_)):
        for j in range(i + 1, len(x_)):
            if i != j:
                heapq.heappush(weights, (math.sqrt((x_[i] - x_[j]) ** 2 + (y_[i] - y_[j]) ** 2), i, j))
    while len(sets) != k:
        distance, x, y = heapq.heappop(weights)
        if get_id(x) != get_id(y):
            sets.remove(get_id(x))
            sets.remove(get_id(y))
            sets.add(join(x, y))
    while weights:
        distance, x, y = heapq.heappop(weights)
        if get_id(x) != get_id(y):
            result = distance
            break
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    rank = [1 for i in range(n)]
    parent = [i for i in range(n)]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
