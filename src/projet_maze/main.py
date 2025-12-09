from .maze import Maze

def main():
    maze = Maze(representation=[
        ['#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '#'],
       ['#', '#', '#', '#', '#']])
    maze.display_maze()
    maze.export('exported_maze.txt')