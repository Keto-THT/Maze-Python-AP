from .maze import Maze

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Maze Generator parameters")
    parser.add_argument('--width', type=int, help='Set the width of the maze to generate')
    parser.add_argument('--height', type=int, help='Set the height of the maze to generate')
    parser.add_argument('--seed', type=str, help='Set the seed of the maze to generate')
    parser.add_argument('--emptiness', type=float, help='Set the emptiness of the maze to generate')
    parser.add_argument('--output', type=str, help='Set the output of the maze to generate')
    args = parser.parse_args()
    print(args.width)
