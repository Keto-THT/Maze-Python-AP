class MazeSolve ():
    def _init__ (self, maze):
        self.maze = maze
        self.enter = self.find_enter(maze)
        self.exit = self.find_exit(maze)

    def maze_solve(self):
        enter, exit = self.enter, self.exit
        chemin = {(enter[0]+1, enter[1]): [(enter[0], enter[1]), (enter[0]+1, enter[1])]}
        chemin_check = {}
        while exit not in chemin:
            if chemin_check == chemin:
                raise Exception ("Pas de solution trouvée à ce labyrinthe.")
            chemin_check = chemin.copy()
            new_chemin = {}
            for case in chemin:
                voisins = [(case[0]+1, case[1]), (case[0]-1, case[1]), (case[0], case[1]+1), (case[0], case[1]-1)]
                for voisin in voisins:
                    if maze[voisin[0]][voisin[1]] == ' ' and voisin not in chemin and voisin not in new_chemin:
                        new_chemin[voisin] = chemin[case] + [voisin]
            chemin.update(new_chemin)

        return chemin[exit]


    def find_enter (self, self.maze):
        for i in range(len(maze[0])):
            if maze[0][i] == ' ':
                return (0,i)

    def find_exit (self):
        for i in range(len(self.maze[-1])):
            if maze[-1][i] == ' ':
                return (len(self.maze)-1,i)
            
