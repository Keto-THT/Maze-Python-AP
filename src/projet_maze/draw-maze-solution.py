import pygame
import sys
from maze_solve import MazeSolve 
from projet_maze.const import CELL_SIZE, COLOR_BG, COLOR_WALL, COLOR_PATH, COLOR_START, COLOR_EXIT


def draw_maze_clean(screen, maze, solution_path, start, end):

    rows = len(maze)
    cols = len(maze[0])

    for r in range(rows):
        for c in range(cols):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            if maze[r][c] == '#':
                pygame.draw.rect(screen, COLOR_WALL, rect)
            else:
                pygame.draw.rect(screen, COLOR_BG, rect)

    if solution_path:
        for (r, c) in solution_path:
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            # On dessine un carré légèrement plus petit pour l'esthétique
            inner_rect = rect.inflate(-4, -4) 
            pygame.draw.rect(screen, COLOR_PATH, inner_rect)

    if start:
        center = (start[1] * CELL_SIZE + CELL_SIZE//2, start[0] * CELL_SIZE + CELL_SIZE//2)
        pygame.draw.circle(screen, COLOR_START, center, CELL_SIZE//3)
    if end:
        center = (end[1] * CELL_SIZE + CELL_SIZE//2, end[0] * CELL_SIZE + CELL_SIZE//2)
        pygame.draw.circle(screen, COLOR_EXIT, center, CELL_SIZE//3)