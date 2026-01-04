
class DetectZone :
    def __init__(self, maze):
        self.maze = maze
        self.grid = maze.get_representation()
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.zones = []

    def is_empty(self, x, y): 
        return self.grid[x][y] != '#'

    def detect_zones(self):
        visited = [[False for i in range(self.width)] for j in range(self.height)]
        for x in range(self.height): 
            for y in range(self.width):
                if self.is_empty(x, y) and not visited[x][y]:
                    zone = []
                    self._explore_zone(x, y, visited, zone)
                    self.zones.append(zone)
                
    def _explore_zone(self, x, y, visited, zone): 
        visited[x][y] = True
        zone.append((x,y))
        for dx, dy in [(-1,0), (1,0), (0, -1), (0,1)]:
            i, j = x + dx, y + dy
            if 0 <= i < self.height and 0 <= j < self.width : 
                if self.is_empty(i,j) and not visited[i][j]:
                    self._explore_zone(i,j,visited,zone)
    
    def print_zones(self):
        for index, zone in enumerate(self.zones):
            print(f"Zone {index + 1} : {zone}")
            for x, y in zone: 
                print(f"({x}, {y})")
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def label_zones(self):
        labeled_grid = [line.copy() for line in self.grid]
        for index, zone in enumerate(self.zones):
            letter = alphabet[index % len(alphabet)]
            for x, y in zone :
                labeled_grid[x][y] = letter
        return labeled_grid
    
    def print_labeled_zones(self):
        labeled_grid = self.label_zones()
        for line in labeled_grid: 
            print(''.join(line))
        