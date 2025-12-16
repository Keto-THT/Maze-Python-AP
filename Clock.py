import pygame
import time

pygame.init()
pygame.font.init()

class Clock: 
    def __init__(self): 
        self.start_time = None
        self.elapsed_time = 0 
        self.font = pygame.font.Sysfont('monospace', 35)
        self.message_color = pygame.Color('yellow')
    
    def start_timer(self):
        self.start_time = time.time()
    
    def update_timer(self):
        if self.start_time is not None: 
            self.elapsed_time = time.time() - self.start_time
    
    def display_timer(self):
        sec = int(self.elapsed_time % 60)
        min = int(self.elapsed_time / 60)
        my_time = self.font.render(f"{min:02}:{sec:02}", True, self.message_color)
        return my_time
    
    def stop_timer(self):
        self.start_time = None