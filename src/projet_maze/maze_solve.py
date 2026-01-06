class MazeSolve:
    def __init__(self, maze):  
        self.maze = maze
        self.enter = self.find_enter()
        self.exit = self.find_exit()

    def maze_solve(self):
        enter, exit = self.enter, self.exit
        # On commence le chemin à l'entrée même
        chemin = {enter: [enter]}
        chemin_check = {}
        
        while exit not in chemin:
            if chemin_check == chemin:
                raise Exception("Pas de solution trouvée à ce labyrinthe.")
            
            chemin_check = chemin.copy()
            new_chemin = {}
            
            for case in chemin:
                voisins = [(case[0]+1, case[1]), (case[0]-1, case[1]), 
                           (case[0], case[1]+1), (case[0], case[1]-1)]
                
                for voisin in voisins:
                    # Vérification des limites du labyrinthe pour éviter les IndexError
                    if 0 <= voisin[0] < len(self.maze) and 0 <= voisin[1] < len(self.maze[0]):
                        if self.maze[voisin[0]][voisin[1]] == ' ' and voisin not in chemin and voisin not in new_chemin:
                            new_chemin[voisin] = chemin[case] + [voisin]
            
            chemin.update(new_chemin)

        return chemin[exit]
    
    def maze_solve2(self):

        frontiere = [self.enter]
        visites = {self.enter: [self.enter]}
        
        while frontiere:
            prochaine_frontiere = []
            for case in frontiere:
                if case == self.exit:
                    return visites[case]

                # Directions : Bas, Haut, Droite, Gauche
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    voisin = (case[0] + dr, case[1] + dc)
                    
                    # Vérification des limites et si c'est un mur
                    if (0 <= voisin[0] < len(self.maze) and 
                        0 <= voisin[1] < len(self.maze[0]) and
                        self.maze[voisin[0]][voisin[1]] == ' ' and
                        voisin not in visites):
                        
                        visites[voisin] = visites[case] + [voisin]
                        prochaine_frontiere.append(voisin)
            
            frontiere = prochaine_frontiere

            if prochaine_frontiere == []:
                raise Exception("Pas de solution trouvée.")

        return visites[self.exit]

    def find_enter(self):
        # Cherche l'entrée sur la première ligne
        for i in range(len(self.maze[0])):
            if self.maze[0][i] == ' ':
                return (0, i)

    def find_exit(self):
        # Cherche la sortie sur la dernière ligne
        for i in range(len(self.maze[-1])):
            if self.maze[-1][i] == ' ':
                return (len(self.maze)-1, i)

def load_maze(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip('\n')) for line in f.readlines()]

def maze_solver():
    mon_labyrinthe = load_maze('maze.txt')
    solveur = MazeSolve(mon_labyrinthe)
    solution = solveur.maze_solve2()
    return("Chemin trouvé :", solution)

