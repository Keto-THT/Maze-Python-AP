def maze_solve(maze):
    enter, exit = find_enter(maze), find_exit(maze)
    chemin = {(enter[0]+1, enter[1]): [(enter[0], enter[1]), (enter[0]+1, enter[1])]}
    while exit not in chemin:
        new_chemin = {}
        for case in chemin:
            voisins = [(case[0]+1, case[1]), (case[0]-1, case[1]), (case[0], case[1]+1), (case[0], case[1]-1)]
            for voisin in voisins:
                if maze[voisin[0]][voisin[1]] == ' ' and voisin not in chemin and voisin not in new_chemin:
                    new_chemin[voisin] = chemin[case] + [voisin]
        chemin.update(new_chemin)
    return chemin[exit]




def find_enter (maze):
    for i in range(len(maze[0])):
        if maze[0][i] == ' ':
            return (0,i)

def find_exit (maze):
    for i in range(len(maze[-1])):
        if maze[-1][i] == ' ':
            return (len(maze)-1,i)
        
