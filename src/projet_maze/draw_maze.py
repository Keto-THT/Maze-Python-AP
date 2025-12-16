import pygame
import sys
from maze_gen import MazeGenerator


cell_size = 30  

#initialisation des couleurs
color_wall = (0, 0, 0)       
color_path = (255, 255, 255) 
color_start = (0, 255, 0)    
color_exit = (255, 0, 0)      

# Fonction pour dessiner le labyrinthe
def draw_maze(screen, maze_rep):
    
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
    maze_width = 15   
    maze_height = 15
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
