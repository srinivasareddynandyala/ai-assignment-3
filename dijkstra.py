import heapq
import csv
from collections import defaultdict

def read_graph(file_name):
    network = defaultdict(dict)

    with open(file_name, 'r') as f:
        data = csv.DictReader(f)
        for item in data:
            start = item['source'].strip()
            end = item['destination'].strip()
            distance = int(item['distance'])

            network[start][end] = distance
            network[end][start] = distance

    return network

def find_shortest_path(network, source):
    shortest = {node: float('inf') for node in network}
    previous = {node: None for node in network}

    shortest[source] = 0
    queue = [(0, source)]

    while queue:
        dist, node = heapq.heappop(queue)

        for next_node in network[node]:
            total = dist + network[node][next_node]

            if total < shortest[next_node]:
                shortest[next_node] = total
                previous[next_node] = node
                heapq.heappush(queue, (total, next_node))

    return shortest, previous

def build_path(previous, target):
    route = []

    while target is not None:
        route.append(target)
        target = previous[target]

    return route[::-1]

graph = read_graph("cities.csv")

source_city = input("Enter start city: ")
target_city = input("Enter destination city: ")

shortest, previous = find_shortest_path(graph, source_city)

if target_city in shortest and shortest[target_city] != float('inf'):
    route = build_path(previous, target_city)
    print("Shortest distance:", shortest[target_city], "km")
    print("Path:", " -> ".join(route))
else:
    print("No path found")
