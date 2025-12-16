
class DetectZone :
    def __init__(self, maze):
        self.maze = maze
        self.grid = maze.get_representation()
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.zones = []

    def is_empty(self, x, y): 
        return self.grid[x][y] != '#'

    def _detect_zones(self):
        visited = [[False for i in range(self.width)] for j in range(sekf.height)]
        for x in range(self.width): 
            for y in range(self.height):
                if self.is_empty(x, y) and not visited[x][y]:
                    zone = []
                    self._explore_zone(x, y, visited, zone)
                    self.zones.append(zone)
                
    def _explore_zone(self, x, y, visited, zone): 
        visited[x][y] = True
        zone.append((x,y))
        for dx, dy in [(-1,0), (1,0), (0, -1), (0,1)]:
            i, j = x + dx, y + dy
            if 0 <= i < self.width and 0 <= j < self.height : 
                if self.is_empty(i,j) and not visited[i][j]:
                    self._explore(i,j,visited,zone)
    
    def print_zones(self):
        for index, zone in enumerate(self.zones):
            print(f"Zone {idx + 1} : {zone}")
            for x, y in zone: 
                print(f"({x}, {y})")