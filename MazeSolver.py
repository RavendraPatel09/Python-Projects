from collections import deque

def parse_maze(lines):
    grid = [list(line) for line in lines]
    start = end = None
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "S":
                start = (r, c)
            elif val == "E":
                end = (r, c)
    return grid, start, end

def solve_maze(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] != "#":
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))
    return None

def main():
    path_file = input("Maze file path: ")
    with open(path_file, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    grid, start, end = parse_maze(lines)
    if not start or not end:
        print("Maze must contain S and E")
        return
    result = solve_maze(grid, start, end)
    if result:
        print(f"Path found with {len(result) - 1} steps")
        print(result)
    else:
        print("No path found")

if __name__ == "__main__":
    main()
