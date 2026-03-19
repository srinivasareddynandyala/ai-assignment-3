import heapq
import random

def find_path(grid, start, goal):
    queue = [(0, start)]
    cost_so_far = {start: 0}
    came_from = {}

    def distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    while queue:
        _, current = heapq.heappop(queue)

        if current == goal:
            route = []
            while current in came_from:
                route.append(current)
                current = came_from[current]
            route.append(start)
            return route[::-1]

        x, y = current

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                next_step = (nx, ny)
                new_cost = cost_so_far[current] + 1

                if next_step not in cost_so_far or new_cost < cost_so_far[next_step]:
                    cost_so_far[next_step] = new_cost
                    priority = new_cost + distance(next_step, goal)
                    heapq.heappush(queue, (priority, next_step))
                    came_from[next_step] = current

    return None

def run_simulation(size):
    grid = [[0 for _ in range(size)] for _ in range(size)]
    start = (0, 0)
    goal = (size - 1, size - 1)
    position = start

    while position != goal:
        if random.random() < 0.2:
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)
            grid[x][y] = 1

        path = find_path(grid, position, goal)

        if not path:
            print("No path available")
            return

        if len(path) > 1:
            position = path[1]

    print("Goal reached")

run_simulation(70)
