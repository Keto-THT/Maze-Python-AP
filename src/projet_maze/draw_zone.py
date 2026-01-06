import pygame
from const import (
    CELL_SIZE
)

ZONE_COLORS = [
    (255, 255, 0),    # jaune
    (255, 0, 255),    # magenta
    (0, 255, 255),    # cyan
    (255, 165, 0),    # orange
    (128, 0, 128),    # violet
    (0, 128, 128),    # teal
    (128, 128, 0),    # olive
]

def draw_zones(screen, detect_zone):
    """
    Dessine chaque zone détectée par DetectZone avec une couleur différente.
    """
    for index, zone in enumerate(detect_zone.zones):
        color = ZONE_COLORS[index % len(ZONE_COLORS)]

        for x, y in zone:
            rect = pygame.Rect(
                y * CELL_SIZE,   # colonne → pixel X
                x * CELL_SIZE,   # ligne → pixel Y
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(screen, color, rect)



    