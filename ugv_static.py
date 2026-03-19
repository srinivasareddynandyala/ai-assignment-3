import heapq
import random

def build_grid(size, obstacle_rate):
    board = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if random.random() < obstacle_rate:
                board[i][j] = 1

    return board

def find_path(board, start, goal):
    queue = [(0, start)]
    cost = {start: 0}
    previous = {}

    def estimate(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    while queue:
        _, current = heapq.heappop(queue)

        if current == goal:
            route = []
            while current in previous:
                route.append(current)
                current = previous[current]
            route.append(start)
            return route[::-1]

        x, y = current

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 0:
                next_cell = (nx, ny)
                new_cost = cost[current] + 1

                if next_cell not in cost or new_cost < cost[next_cell]:
                    cost[next_cell] = new_cost
                    priority = new_cost + estimate(next_cell, goal)
                    heapq.heappush(queue, (priority, next_cell))
                    previous[next_cell] = current

    return None

grid = build_grid(70, 0.25)
start = (0, 0)
goal = (69, 69)

path = find_path(grid, start, goal)

if path:
    print("Path length:", len(path))
else:
    print("No path found")
