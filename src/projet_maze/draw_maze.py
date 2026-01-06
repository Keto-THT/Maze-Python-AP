import pygame
import sys
from maze_gen import MazeGenerator

from .const import COLOR_WALL, COLOR_PATH, COLOR_START, COLOR_EXIT, CELL_SIZE

cell_size = CELL_SIZE
color_wall = COLOR_WALL
color_path = COLOR_PATH
color_start = COLOR_START
color_exit = COLOR_EXIT

class MazeDrawer:
    def __init__(self, maze, cell_size=20):
        self.maze = maze
        self.cell_size = cell_size
        self.maze_rep = maze.get_representation()

        self.rows = len(self.maze_rep)
        self.cols = len(self.maze_rep[0])
        
        self.width = self.cols * self.cell_size
        self.height = self.rows * self.cell_size
        

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Maze Drawer")


    def draw_maze(self):    
        rows = len(maze_rep)
        cols = len(maze_rep[0])

        for y in range(rows):
            for x in range(cols):
                cell = maze_rep[y][x]
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)

                if cell == '#':
                    pygame.draw.rect(screen, color_wall, rect)
                elif cell == ' ':
                    pygame.draw.rect(screen, color_path, rect)
                elif cell == 'E': 
                    pygame.draw.rect(screen, color_start, rect)
                elif cell == 'S': 
                    pygame.draw.rect(screen, color_exit, rect)
                else:
                    pygame.draw.rect(screen, color_path, rect)
            


def main():
    #dimensions du labyrinthe 
    maze_width = 10  
    maze_height = 10
    seed = None

    #génération du labyrinthe
    generator = MazeGenerator(width=maze_width, height=maze_height, seed= seed)
    maze = generator.generate_maze()
    maze_rep = maze.get_representation()
    
    #récupérer la représentation du labyrinthe
    grid_h = len(maze_rep)
    grid_w = len(maze_rep[0])
    screen_width = grid_w * cell_size
    screen_height = grid_h * cell_size

    #initialisation pygame
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(f"Générateur de Labyrinthe ({grid_w}x{grid_h})")

    #boucle de commande
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
  
        screen.fill(color_wall) 
        draw_maze(screen, maze_rep)
        
    
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
