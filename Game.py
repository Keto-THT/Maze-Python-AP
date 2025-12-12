import pygame

pygame.init()
pygame.font.init()

class Game: 
    def __init__(self, winning_cell, tile):
        self.font = pygame.font.Sysfont("impact", 35)
        self.message_color = pygame.Color("darkblue")
        self.winning_cell = winning_cell
        self.tile = tile


    def win(self):
        msg = self.font.render('Tu as gagné !', True, self.message_color)
    
    def is_game_over(self, player):
        winning_cell_x, winning_cell_y = self.winning_cell.x * tile, self.winning_cell.y * tile
        if player.x >= winning_cell_x and player.y >= winning_cell_y:
            return True
        else : 
            return False