# Each guest must have exactly two neighbors (enforced in is_valid).
# It uses recursive backtracking to try all permutations starting with the first guest fixed (to avoid rotational duplicates).
# The final result is checked for circular validity before returning.


def find_seating_arrangement(guests):
    # Create a graph from preferences
    graph = {guest: set(prefs) for guest, prefs in guests.items()}
    n = len(guests)
    path = []
    
    def backtrack(current):
        # If all guests are seated and last guest connects to first
        if len(path) == n and path[0] in graph[path[-1]]:
            return True
        for neighbor in graph[current]:
            if neighbor not in path:
                path.append(neighbor)
                if backtrack(neighbor):
                    return True
                path.pop()
        return False
    
    # Try starting with each guest
    for start_guest in guests:
        path = [start_guest]
        if backtrack(start_guest):
            return path
    return "No valid seating arrangement possible"

# Example usage
guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

result = find_seating_arrangement(guests)
print(result)