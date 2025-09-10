
import heapq
from collections import defaultdict
import random

# Define the city grid and graph properties
GRID_SIZE = 10  # 10x10 grid
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up


# Generate graph with edge weights
def create_city_graph(grid_size):
    print("Creating city graph...", flush=True)
    graph = defaultdict(list)
    for x in range(grid_size):
        for y in range(grid_size):
            node = (x, y)
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
                    # Simulate traffic: normal = 1 min, heavy = 2-3 min
                    weight = random.uniform(1, 3) if random.random() < 0.3 else 1
                    graph[node].append(((new_x, new_y), weight))
    print(f"Graph created with {len(graph)} nodes.", flush=True)
    return graph


# Manhattan distance heuristic
def heuristic(node, goal):
    return (abs(node[0] - goal[0]) + abs(node[1] - goal[1])) / 60


# A* algorithm
def a_star(start, goal, graph):
    print(f"Running A* from {start} to {goal}...", flush=True)
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    iteration = 0
    max_iterations = 10000  # Prevent infinite loops

    while open_set and iteration < max_iterations:
        iteration += 1
        if iteration % 1000 == 0:
            print(f"Iteration {iteration}, open set size: {len(open_set)}", flush=True)

        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            print(f"Path found after {iteration} iterations.", flush=True)
            return path[::-1], g_score[goal]

        for neighbor, weight in graph[current]:
            tentative_g_score = g_score[current] + weight

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    print("No path found.", flush=True)
    return None, float('inf')


# Main function
def ambulance_dispatch(start, goal):
    print("Starting ambulance dispatch...", flush=True)
    if not (0 <= start[0] < GRID_SIZE and 0 <= start[1] < GRID_SIZE):
        print(f"Invalid start position: {start}", flush=True)
        return None, float('inf')
    if not (0 <= goal[0] < GRID_SIZE and 0 <= goal[1] < GRID_SIZE):
        print(f"Invalid goal position: {goal}", flush=True)
        return None, float('inf')

    graph = create_city_graph(GRID_SIZE)
    path, total_cost = a_star(start, goal, graph)

    if path:
        print(f"Optimal path found: {path}", flush=True)
        print(f"Estimated travel time: {total_cost:.2f} minutes", flush=True)
    else:
        print("No path found to the emergency location.", flush=True)
    return path, total_cost


# Example usage
if __name__ == "__main__":
    print("Script started", flush=True)
    start = (0, 0)
    goal = (9, 9)
    random.seed(42)
    ambulance_dispatch(start, goal)
