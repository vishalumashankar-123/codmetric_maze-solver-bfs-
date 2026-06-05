from collections import deque

# BFS Function
def bfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path

        if (x, y) in visited:
            continue

        visited.add((x, y))

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and
                0 <= ny < cols and
                maze[nx][ny] != "#" and
                (nx, ny) not in visited):

                queue.append(((nx, ny), path + [(nx, ny)]))

    return None

# Display Maze with Solution Path
def display_maze(maze, path):
    maze_copy = [row[:] for row in maze]

    if path:
        for x, y in path:
            if maze_copy[x][y] not in ["S", "E"]:
                maze_copy[x][y] = "*"

    print("\nMaze Solution:\n")
    for row in maze_copy:
        print(" ".join(row))

# Test Maze
maze = [
    ['S', '.', '.', '#', '.', '.'],
    ['#', '#', '.', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '#', 'E']
]

start = (0, 0)
end = (4, 5)

path = bfs(maze, start, end)

if path:
    print("Shortest Path Found!")
    print("Path Length:", len(path) - 1)
    display_maze(maze, path)
else:
    print("No path found!")