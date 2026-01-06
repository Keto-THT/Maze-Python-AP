import pygame



from maze import Maze
from maze_gen import MazeGenerator
from maze_detect import DetectZone
from maze_solve import MazeSolve

from draw_zone import draw_zones
from draw_maze_solution import draw_maze_solution

from const import (
    SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE,
    COLOR_BG, COLOR_WALL, COLOR_PATH, COLOR_START, COLOR_EXIT,
    MAZE_ROWS, MAZE_COLS
)

def main():

    gen_w = (MAZE_COLS - 1) // 2
    gen_h = (MAZE_ROWS - 1) // 2
    
    #génération du labyrinthe
    generator = MazeGenerator(width=gen_w, height=gen_h)
    maze_obj = generator.generate_maze()
    maze_obj.export("maze.txt") # Sauvegarde dans le fichier maze.txt

    # nettoyage de la grille 
    raw_grid = maze_obj.get_representation()
    grid_clean = [line[:] for line in raw_grid]
    
    start_pos = None
    end_pos = None
    rows = len(grid_clean)
    cols = len(grid_clean[0])

    #parcours de la grille pour trouver E et S
    for r in range(rows):
        for c in range(cols):
            if grid_clean[r][c] == 'E':
                start_pos = (r, c)
                grid_clean[r][c] = ' ' # On transforme E en espace
            elif grid_clean[r][c] == 'S':
                end_pos = (r, c)
                grid_clean[r][c] = ' ' # On transforme S en espace

    # on recrée un objet Maze avec la grille nettoyée
    maze_logic = Maze(representation=grid_clean)

    #on chercher les zones connexes
    detector = DetectZone(maze_logic)
    detector.detect_zones()
    print(f"{len(detector.zones)} zone(s) trouvée(s)")


    #on cherche la solution du labyrinthe
    solveur = MazeSolve(grid_clean) # MazeSolve prend la grille (list de list)
    try:
        solution_path = solveur.maze_solve()
        print("Solution trouvée")
    except Exception as e:
        print(f" -> Erreur/Info : {e}")
        solution_path = []

    #affichage avec pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Projet Maze - Zones & Solution")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(COLOR_BG)

        #on dessine les zones et la solution
        draw_zones(screen, detector)
        draw_maze_solution(screen, raw_grid, solution_path)


        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()