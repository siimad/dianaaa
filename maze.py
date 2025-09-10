from collections import deque


def bfs(maze, start, goal):
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    queue.append(start)

    visited = set()
    visited.add(start)

    parent = {}
    parent[start] = None

    while queue:
        current = queue.popleft()
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for dx, dy in directions:
            next_x = current[0] + dx
            next_y = current[1] + dy
            next_node = (next_x, next_y)

            if next_x < 0 or next_x >= len(maze) or next_y < 0 or next_y >= len(maze[0]):
                continue

            if maze[next_x][next_y] == 0 and next_node not in visited:
                visited.add(next_node)
                parent[next_node] = current
                queue.append(next_node)

    return None


# INPUT DATA
maze = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

# RUN THE ALGORITHM
path = bfs(maze, start, goal)

# OUTPUT THE RESULT
if path:
    print("Path found!")
    print("Number of moves:", len(path) - 1)
    print("Path:", path)
else:
    print("No path exists!")