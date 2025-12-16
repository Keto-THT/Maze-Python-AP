from maze import Maze
import random

class MazeGenerator:
    def __init__(self, width: int, height: int, seed: int | None = None):
        self.width = width
        self.height = height
        self.seed = seed

    def _set_entrance_and_exit(self, representation: list):
        rng = random.Random(self.seed)
        entrance = rng.randrange(1, 2 * self.width, 2)
        exit = rng.randrange(1, 2 * self.height, 2)
        representation[0][entrance] = 'E'
        representation[2 * self.height][exit] = 'S'
        if representation[1][entrance] == '#' or representation[2 * self.height - 1][exit] == '#':
            return self._set_entrance_and_exit(representation)
        return representation

    def generate_maze(self):
        rng = random.Random(self.seed)
        grid_width = 2 * self.width + 1
        grid_height = 2 * self.height + 1
        representation = [['#' for _ in range(grid_width)] for _ in range(grid_height)]
        visited = [[False for _ in range(self.width)] for _ in range(self.height)]

        def generate_maze_aux(x: int, y: int):
            visited[y][x] = True
            gx, gy = 2 * x + 1, 2 * y + 1
            representation[gy][gx] = ' '
            directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            rng.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and not visited[ny][nx]:
                    wall_x = gx + dx
                    wall_y = gy + dy
                    representation[wall_y][wall_x] = ' '
                    generate_maze_aux(nx, ny)

        start_x = rng.randrange(self.width)
        start_y = rng.randrange(self.height)
        generate_maze_aux(start_x, start_y)

        representation = self._set_entrance_and_exit(representation)
        maze = Maze(representation=representation)

        return maze


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Maze Generator parameters")
    parser.add_argument('--width', '-w', type=int, help='Set the width of the maze to generate')
    parser.add_argument('--height', '-H', type=int, help='Set the height of the maze to generate')
    parser.add_argument('--seed', '-s', type=int, help='Set the seed of the maze to generate')
    parser.add_argument('--emptiness', '-e', type=float, help='Set the emptiness of the maze to generate')
    parser.add_argument('--output', '-o', type=str, help='Set the output of the maze to generate')
    args = parser.parse_args()

    maze = MazeGenerator(args.width, args.height, args.seed).generate_maze()
    maze.export(args.output)


if __name__ == "__main__":
    main()