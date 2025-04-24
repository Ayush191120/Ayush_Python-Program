import heapq

def dijkstra(graph, start, end):
    # Priority queue: (distance, city, path_so_far)
    heap = [(0, start, [start])]
    visited = set()

    while heap:
        current_dist, current_city, path = heapq.heappop(heap)

        if current_city in visited:
            continue
        visited.add(current_city)

        if current_city == end:
            return path, current_dist

        for neighbor, weight in graph[current_city].items():
            if neighbor not in visited:
                heapq.heappush(heap, (current_dist + weight, neighbor, path + [neighbor]))

    return None, float('inf')  # No path found

# Example graph
cities = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 9, 'C': 1}
}

start_city = 'A'
destination_city = 'D'

path, distance = dijkstra(cities, start_city, destination_city)

if path:
    print(f"Shortest path from {start_city} to {destination_city}: {' -> '.join(path)}")
    print(f"Total distance: {distance}")
else:
    print("No path found.")
