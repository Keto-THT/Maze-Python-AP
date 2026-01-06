import pygame

from const import CELL_SIZE, COLOR_WALL, COLOR_PATH, COLOR_START, COLOR_EXIT

def draw_maze_solution(screen, maze, solution_path=None):
    """
    dessine les murs du labyrinthe et le chemin de la solution si elle existe
    """
    rows = len(maze)
    cols = len(maze[0])
    
    start_pos = None
    end_pos = None

    #on dessine les murs et on en profite pour repérer l'entrée et la sortie
    for r in range(rows):
        for c in range(cols):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            cell_value = maze[r][c]
            
            if cell_value == '#':
                pygame.draw.rect(screen, COLOR_WALL, rect)
            
            
            if cell_value == 'E':
                start_pos = (r, c)
            elif cell_value == 'S':
                end_pos = (r, c)

    #dessiner la solution si elle existe
    if solution_path:
        for (r, c) in solution_path:
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            rect_petit = rect.inflate(-10, -10) 
            pygame.draw.rect(screen, COLOR_PATH, rect_petit)

    #dessiner l'entrée et la sortie
    if start_pos:
        center = (start_pos[1] * CELL_SIZE + CELL_SIZE//2, start_pos[0] * CELL_SIZE + CELL_SIZE//2)
        pygame.draw.circle(screen, COLOR_START, center, CELL_SIZE//3)
    
    if end_pos:
        center = (end_pos[1] * CELL_SIZE + CELL_SIZE//2, end_pos[0] * CELL_SIZE + CELL_SIZE//2)
        pygame.draw.circle(screen, COLOR_EXIT, center, CELL_SIZE//3)