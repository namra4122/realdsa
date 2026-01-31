import heapq
import sys


def paths(source: int, adjList: list) -> list:
    # Distance list
    distance = [sys.maxsize] * len(adjList)
    visited = [0] * len(adjList)
    distance[source] = 0  # Make source distance zero

    # Priority queue
    queue = []
    heapq.heappush(queue, (0, source))  # Push source node in queue

    while len(queue) > 0:
        d, n = heapq.heappop(queue)

        if visited[n]:
            continue

        visited[n] = 1

        for x, y in adjList[n]:
            if distance[n] + y < distance[x]:
                distance[x] = distance[n] + y
                heapq.heappush(queue, (distance[x], x))

    return distance


def findPath(start: int, end: int, adjList: list) -> tuple[int, str]:
    dist = 0
    path = ""

    dist_array = paths(start, adjList)

    dist = dist_array[end]
    print(dist_array)

    return (dist, path)


adjList = [
    # [(1, 4), (2, 3)],
    # [(0, 4), (4, 6)],
    # [(0, 8), (3, 2)],
    # [(2, 2), (4, 10)],
    # [(1, 6), (3, 10)],
    # [(1, 4), (2, 8)],
    # [(4, 6)],
    # [(1, 3), (3, 2)],
    # [],
    # [(3, 10)],
    [(1,5), (2,1)],
    [(0,5),(2,1)],
    [(0,1),(1,1)],
]

dist = findPath(0, 1, adjList)
print(dist)
