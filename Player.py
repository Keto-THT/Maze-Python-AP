import pygame

pygame.init()
pygame.font.init()

class Player : 

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.player_size = 10
        self.rect = pygame.Rect(int(self.x), int(self.y), self.player_size, self.player_size)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.rigt_pressed = False
        self.up_pressed_pressed = False
        self.down_pressed = False
        self.speed = 4

    def get_current_cell(self, x, y, grid_cells):
        for cell in grid_cells:
            if cell.x == x and cell.y == y:
                return cell
    
    def check_move(self, tile, grid_cells):


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def update(self):
        self.velX = 0 
        self.velY = 0 

        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed

        if self.up_pressed and not self.down_pressed:
            self.velY = self.speed
        
        if self.down_pressed and not self.up_pressed:
            self.velY = -self.speed

        self.x += self.velX
        self.y += self.velY
        self.rect = pygame.Rect(int(self.x), int(self.y), self.player_size, self.player_size)

