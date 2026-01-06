
class DetectZone :
    def __init__(self, maze):
        self.maze = maze
        self.grid = maze.get_representation()
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.zones = []

    def is_empty(self, i, j): 
        return self.grid[i][j] == ' '

    def detect_zones(self):
        visited = [[False for i in range(self.width)] for j in range(self.height)]
        for i in range(self.height): 
            for j in range(self.width):
                if self.is_empty(i, j) and not visited[i][j]:
                    zone = []
                    self._explore_zone(i, j, visited, zone)
                    self.zones.append(zone)
                
    def _explore_zone(self, i, j, visited, zone): 
        visited[i][j] = True
        zone.append((i-1,j-1)) #Car dans l'exemple on ne compte pas les bords dans l'abcisse et l'ordonnée
        for dx, dy in [(-1,0), (1,0), (0, -1), (0,1)]:
            n, m = i + dx, j + dy
            if 0 <= n < self.height and 0 <= m < self.width : 
                if self.is_empty(n,m) and not visited[n][m]:
                    self._explore_zone(n,m,visited,zone)
    
    def print_zones(self):
        for index, zone in enumerate(self.zones):
            print(f"Zone {index + 1}")
            for x, y in zone: 
                print(f"({x}, {y})")
    
    alphabet = 'abcdefghijklmopqrstuvwxyz'

    def label_zones(self):
        labeled_grid = [line.copy() for line in self.grid]
        for index, zone in enumerate(self.zones):
            letter = self.alphabet[index % len(self.alphabet)]
            for x, y in zone :
                labeled_grid[x][y] = letter
        return labeled_grid
    
    def print_labeled_zones(self):
        labeled_grid = self.label_zones()
        for line in labeled_grid: 
            print(''.join(line))
        
